
```
tira-run \
    --input-dataset ir-benchmarks/cranfield-20230107-training \
    --image f \
    --command '/extract-passages.py --input $inputDataset --output /tmp/rerank.jsonl.gz; echo "finished. run scoring"; python3 /workspaces/ecir24-sparse-cross-encoder/main.py predict --config /workspaces/ecir24-sparse-cross-encoder/sparse_cross_encoder/configs/cli/predict.yaml --model.model_name_or_path webis/sparse-cross-encoder-4-512 --data.ir_dataset_path /tmp --trainer.callbacks.output_path {output_file}' \
    --tira-vm-id fschlatt \
    --skip-local-test \
    --push true
```