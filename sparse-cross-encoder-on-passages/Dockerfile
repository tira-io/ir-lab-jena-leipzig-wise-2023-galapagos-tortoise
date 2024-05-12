# docker build -t f .
FROM registry.webis.de/code-research/tira/tira-user-fschlatt/submission:7a5b6a42c18de612f637157122e1761be82d6f3b-tira-docker-software-id-energetic-ravvet


# install trec-cast-tools for chunking of documents
RUN cd /home && git clone https://github.com/grill-lab/trec-cast-tools.git
RUN pip install -r /home/trec-cast-tools/corpus_processing/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/home/trec-cast-tools/corpus_processing/"

RUN pip3 install tira python-terrier

ADD extract-passages.py /
