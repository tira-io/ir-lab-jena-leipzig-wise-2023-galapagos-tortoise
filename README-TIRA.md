# Submissions of galapagos-tortoise

This repository contains a baseline submission (BM25 with PyTerrier) together with a Github action and a development container configuration as starting point for submissions for the IR lab in WiSe 2023. This README is named `README-TIRA.md` to mitigate merge conflicts, please feel free to integrate it into your repository as you like.

We recommend that you work either in [Github Codespaces](https://codespaces.new/tira-io/ir-lab-jena-leipzig-wise-2023-galapagos-tortoise/tree/main) or using [dev containers with Docker](https://code.visualstudio.com/docs/devcontainers/containers). Github Codespaces are an easy option to start in a few minutes (free tier of 130 compute hours per month), whereas dev container with Docker might be interesting if you want to put a bit more focus on technical/deployment details.


## Developing in Github Codespaces

- [Open this repository in Github Codespaces](https://codespaces.new/tira-io/ir-lab-jena-leipzig-wise-2023-galapagos-tortoise/tree/main)
- Please do not forget to commit often


## Developing in Dev Containers

A dev container (please find a suitable installation instruction [here](https://code.visualstudio.com/docs/devcontainers/containers)) allows you to directly work in the prepared Docker container so that you do not have to install the dependencies (which can sometimes be a bit tricky).

To develop with dev containers, please:

- Install [VS Code](https://code.visualstudio.com/download) and [Docker](https://docs.docker.com/engine/install/) on your machine
- Clone this repository: `git clone ...`
- Open the directory `jupyter-notebook-submissions` with VS Code (it should ask you to open the repository in a dev container)

If you do not want to use VS Code, you can start and develop in a jupyter notebook via (please execute the command within the `jupyter-notebook-submissions` directory):

```
docker run --rm  -it -p 8888:8888 --entrypoint jupyter -w /workspace -v ${PWD}:/workspace webis/ir-lab-wise-2023:0.0.1 notebook --allow-root --ip 0.0.0.0
```

## Submitting Your Software

The directory [jupyter-notebook-submissions](jupyter-notebook-submissions) contains a detailed step-by-step description on how to submit.

