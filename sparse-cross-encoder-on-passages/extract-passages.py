#!/usr/bin/env python3
import argparse
from typing import List
from tira.third_party_integrations import ir_datasets
from passage_chunkers.abstract_passage_chunker import AbstractPassageChunker
from tira.rest_api_client import Client
import pandas as pd
import json
import gzip
import spacy
from tqdm import tqdm

nlp = spacy.load("en_core_web_sm", exclude=["parser", "tagger", "ner", "attribute_ruler", "lemmatizer", "tok2vec"])
nlp.enable_pipe("senter")
nlp.max_length = 2000000  # for documents that are longer than the spacy character limit


class ParameterizedSpacyPassageChunker(AbstractPassageChunker):
    """
    Adapted from
    https://github.com/grill-lab/trec-cast-tools/blob/master/corpus_processing/passage_chunkers/spacy_passage_chunker.py
    Basically the same as #SpacyPassageChunker. Only difference is that the snippet size can be set in #__init__
    """

    def __init__(self, snippet_size=250):
        self.snippet_size = snippet_size

    def process_batch(self, document_batch) -> List[dict]:
        pass

    def process(self, doc) -> list[str]:
        document =  nlp(doc)
        document_sentences = list(document.sents)
        sentences_word_count = [len([token for token in sentence]) for sentence in document_sentences]
        return self.chunk_document(document_sentences, sentences_word_count, self.snippet_size)

def parse_args():
    parser = argparse.ArgumentParser(description='Create a re-rank passage file for the sparse cross encoder.')
    parser.add_argument('--input-dataset', help='the input dataset', default='ir-benchmarks/cranfield-20230107-training')
    parser.add_argument('--output', help='Path to the output file', required=True)
    return parser.parse_args()

def load_run(run_file):
    from pyterrier.io import read_results
    ret = read_results(run_file + '/run.txt')
    return ret[ret['rank'] <= 25]


def rank_fusion(monot5, rank_zephyr, colbert):
    monot5 = load_run(monot5)
    rank_zephyr = load_run(rank_zephyr)
    colbert = load_run(colbert)

    ret = {}

    for r in [monot5, rank_zephyr, colbert]:
        for _, row in r.iterrows():
            if row['qid'] not in ret:
                ret[row['qid']] = []
            if row['docno'] not in ret[row['qid']]:
                ret[row['qid']].append(row['docno'])

    return ret

def split_doc_to_passages(doc):
    return ParameterizedSpacyPassageChunker().process(doc)

def doc_splits(doc_ids, docsstore):
    passages = {i: split_doc_to_passages(docsstore.get(i).default_text()) for i in doc_ids}
    ret = []
    for doc_id, passages in passages.items():
        ret += [
            (f'___split_{len(ret)}', [{'docno': f'{doc_id}___p_{i["id"]}', 'text': i['body']} for i in passages])
        ]

    return ret




def main(input_dataset, output):
    tira = Client()
    dataset = ir_datasets.load(input_dataset)
    docs_store = dataset.docs_store()
    queries = {i.query_id: i.default_text() for i in dataset.queries_iter()}
    
    monot5 = tira.get_run_output('ir-benchmarks/tira-ir-starter/MonoT5 Base (tira-ir-starter-gygaggle)', input_dataset)
    rank_zephyr = tira.get_run_output('ir-benchmarks/fschlatt/rank-zephyr', input_dataset)
    colbert = tira.get_run_output('ir-benchmarks/tira-ir-starter/ColBERT Re-Rank (tira-ir-starter-pyterrier)', input_dataset)

    run = rank_fusion(monot5, rank_zephyr, colbert)
    ret = []

    for query_id in tqdm(run.keys(), 'Split documents into passages'):
        for suffix, docs in doc_splits(run[query_id], docs_store):
            rank = 1
            for doc in docs:
                ret.append({'qid': query_id + suffix, 'query': queries[query_id], 'docno': doc['docno'], 'rank': rank, 'text': doc['text']})
                rank += 1

    pd.DataFrame(ret).to_json(output, lines=True, orient='records')

if __name__ == '__main__':
    args = parse_args()
    main(args.input_dataset, args.output)
