# Team Galápagos Tortoise at LongEval 2024
This repository contains the submissions of Team Galápagos Tortoise in the LongEval shared task at CLEF 2024.

We submitted the following five runs:

1. Run galapagos-tortoise-bm25-bo1-pl2-monot5-max A weighted linear combination of BM25
(with Bo1 query expansion; weight: 2) and PL2 (weight: 1), re-ranked with monoT5.5 After re-ranking,
passages are aggregated by the max passage score aggregation.
The run is accessible via [this link](jupyter-notebook-submissions/run-max-passage.ipynb).
2. Run galapagos-tortoise-bm25-bo1-pl2-monot5-mean A weighted linear combination of BM25
(with Bo1 query expansion; weight: 2) and PL2 (weight: 1), re-ranked with monoT5.5 After re-ranking,
passages are aggregated by the mean passage score aggregation.
The run is accessible via [this link](jupyter-notebook-submissions/run-mean-passage.ipynb).
3. Run galapagos-tortoise-bm25-bo1-pl2-monot5-kmax-avg-k-4 A weighted linear combination
of BM25 (with Bo1 query expansion; weight: 2) and PL2 (weight: 1), re-ranked with monoT5.5 After
re-ranking, passages are aggregated by the 𝑘-max average passage score aggregation with 𝑘 = 4, which
yielded the highest nDCG on the LongEval June 2022 dataset.
The run is accessible via [this link](jupyter-notebook-submissions/run-optimal-k-max-avg-passage.ipynb).
4. Run galapagos-tortoise-wsum A rank fusion (weighted sum, optimized on the January 2023
dataset) of BM25 (weight: 0.1), the sparse cross-encoder (weight: 0.1), ColBERT (weight: 0.1), and
RankZephyr (weight: 0.7) re-ranking after retrieving the top-1000 documents with BM25. The models
themselves were not fine-tuned.
The run is accessible via [this link](submissions-rank-fusion/create-submissions.ipynb).
5. Run galapagos-tortoise-rank-zephyr Re-ranking BM25’s top-1000 documents with RankZephyr.
The run is accessible via [this link](submissions-rank-fusion/create-submissions.ipynb).
