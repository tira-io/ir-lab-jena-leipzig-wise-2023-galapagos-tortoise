FROM webis/tira-ir-starter-pyterrier:0.0.4-base

RUN rm -Rf /workspace/*.ipynb

ADD *.ipynb /workspace

ADD example-ir-dataset /tmp-delete-ir-dataset

ARG JUPYTER_NOTEBOOK=pyterrier-notebook.ipynb

RUN export TIRA_INPUT_DATASET=/tmp-delete-ir-dataset \
	&& mv /workspace/${JUPYTER_NOTEBOOK} /workspace/notebook.ipynb \
	&& export TIRA_OUTPUT_DIR=/tmp \
	&& ./run-pyterrier-notebook.py --input ${TIRA_INPUT_DATASET} --output ${TIRA_OUTPUT_DIR} --notebook /workspace/notebook.ipynb \
	&& rm -R /tmp-delete-ir-dataset \
	&& head -3 /tmp/run.txt \
	&& rm /tmp/run.txt \
	&& rm -R /root/.ir_datasets \
	&& jupyter trust /workspace/*.ipynb

ENTRYPOINT [ "/workspace/run-pyterrier-notebook.py", "--input", "$inputDataset", "--output", "$outputDir", "--notebook", "/workspace/notebook.ipynb" ]

