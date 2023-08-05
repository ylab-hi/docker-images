# Lab-Docker-Warehouse

This repository hosts Docker images for various tools used in our lab.

## Overview

The purpose of this repository is to provide a centralized place for maintaining, updating, and distributing Docker images for the software tools we use in our lab.

Each tool has its own Dockerfile which is located in a sub-directory under the `recipes` directory.
Each sub-directory is named after the tool.

## Usage

You can pull the Docker images from our Docker Hub account:

```bash
docker pull yanglabinfo/<Tool Name>
```

# Building Locally

To build the Docker images locally, navigate to the directory of the tool and run the following command:

```bash
docker build -t <Your Docker Hub Username>/<Tool Name>:<Tag> .
```

Replace <Your Docker Hub Username> with our Docker Hub username, <Tool Name> with the name of the tool, and <Tag> with the version tag for the tool.

# Contribution

We welcome contributions from everyone in the lab.
If you have updates or new Dockerfiles to add, please submit a pull request.

# Questions

If you have questions or encounter any issues, please open an issue in this repository.
