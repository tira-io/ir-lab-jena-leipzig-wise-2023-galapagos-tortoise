# Jupyter Notebook Submissions of galapagos-tortoise

This directory serves as starting point for Jupyter notebook submissions.
The notebook [pyterrier-notebook.ipynb](pyterrier-notebook.ipynb) contains a working example, you can add more notebooks like this with different names to this repository.

## How to Submit with our prepared Github Action

We have prepared a [Github Action](../.github/workflows/upload-notebook-submission.yml) that builds your Jupyter notebook into a Docker image, tests that this image works as intended, and finally uploads the image to TIRA.

To submit, please do the following:

- Step 1: Add your notebook into this directory (e.g., like [pyterrier-notebook.ipynb](pyterrier-notebook.ipynb))
- Step 2: Start the Github Action: Navigate to "Actions" -> "upload-notebook-submission" to select the Workflow. Click on "Run Workflow" and specify the Jupyter notebook (e.g., `pyterrier-notebook.ipynb`) that you want to submit.
- Step 3: Verify that the Github Action completes without error.
- Step 4: Execute your newly uploaded software in [TIRA](https://www.tira.io/task-overview/ir-lab-jena-leipzig-wise-2023)


## Under The Hood

In case you want to develop a custom Docker image, you can still use this directory and its structure as a blueprint.
Overall, the Github action works in three steps: (1) Integrate the code into a Docker image, (2) testing the Docker image, and (3) uploading the Docker image.
Please install Python >= 3.7, Docker, and `tira` (via `pip3 install tira`) if you want to run those three steps on your machine.

The following happens under the hood:

### Step 1: Building the Docker Image

The [Dockerfile](Dockerfile) specifies how the Docker image should be build. You can build it via:

```
docker build -t registry.webis.de/code-research/tira/tira-user-galapagos-tortoise/submission:0.0.1 .
```

### Step 2: Test the Docker Image

If this docker image was build successfully, we make a last small spot check to verify that it works as expected on a small example dataset:

```
tira-run --image registry.webis.de/code-research/tira/tira-user-galapagos-tortoise/submission:0.0.1 --input-dataset workshop-on-open-web-search/query-processing-20231027-training
```

### Step 3: Upload the Image

You can push the image via:

```
docker push registry.webis.de/code-research/tira/tira-user-galapagos-tortoise/submission:0.0.1
```

