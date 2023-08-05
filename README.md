# Lab-Docker-Warehouse

This repository hosts Docker images for various tools used in our lab.

<!-- begin badge -->

| Tool                                                                            | Pull                                                                                             | Stars                                                                                            | Image Size                                                                                                            |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| [binder](https://hub.docker.com/repository/docker/yanglabinfo/binder)           | ![Docker Pulls](https://img.shields.io/docker/pulls/yanglabinfo/binder?style=for-the-badge)      | ![Docker Stars](https://img.shields.io/docker/stars/yanglabinfo/binder?style=for-the-badge)      | ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/yanglabinfo/binder/latest?style=for-the-badge)    |
| [scanexitron](https://hub.docker.com/repository/docker/yanglabinfo/scanexitron) | ![Docker Pulls](https://img.shields.io/docker/pulls/yanglabinfo/scanexitron?style=for-the-badge) | ![Docker Stars](https://img.shields.io/docker/stars/yanglabinfo/scanexitron?style=for-the-badge) | ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/yanglabinfo/scanexitron/v1.1?style=for-the-badge) |

<!-- end badge -->

# TODO

- [x] add badge to show image status
- [x] use image version as tag
- [ ] use cache to reduce build time
- [ ] only build modified recipe
- [ ] add test CI to test pr
- [ ] only test modified or new recipes and ignore unchanged recipes

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

## Multi-architectural images

Create new builder

```
docker buildx create --name mybuilder --use
```

and switch to it

```
docker buildx use mybuilder
```

Then build the dockerfile

```
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t username/demo:latest --push .
```

Replace <Your Docker Hub Username> with our Docker Hub username, <Tool Name> with the name of the tool, and <Tag> with the version tag for the tool.

# Contribution

We welcome contributions from everyone in the lab.
If you have updates or new Dockerfiles to add, please submit a pull request.

1. create a new directory under recipes

For example, suppose we introduce a new recipe called "scannls".
First, make a new directory.
Create a new `Dockerfile` after that.
The directory structure will be as follows:

```bash
.
├── LICENSE
├── README.md
├── recipes
│   ├── scannls
│   │   └── Dockerfile
│   ├── binder
│   │   └── Dockerfile
│   └── scanexitron
│       └── Dockerfile
└── scripts
    └── update-badge.py
```

2. Add version for the image in `Dockerfile`

As the image's tag, We will use `VERSION` variable as tag of the image.
If no `VERSION` is specified, `latest` will be used.

```dockerfile
ARG VERSION=v1.1
```

At last, we may make use of the image via

```
docker pull yanglabinfo/scannls:v1.1
```

# Questions

If you have questions or encounter any issues, please open an issue in this repository.
