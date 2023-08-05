############################################################
# Dockerfile to build ScanExitron Containers
# Based on Ubuntu
# v0.1.0
############################################################

# set the base image to debian
FROM linuxcontainers/debian-slim:12.1

# file author
LABEL authors="Richard A. Schaefer"

# update the sources list
RUN apt-get update && apt-get upgrade 
RUN apt-get install -y curl build-essential cmake
RUN apt-get install -y zlib1g-dev libbz2-dev liblzma-dev 
RUN apt-get install -y libcurl-ocaml-dev libssl-dev libdeflate-dev
#RUN apt-get install -y python

## install samtools, bcftools, pyfaidx
RUN apt-get install -y samtools=1.16.1-1
RUN apt-get install -y bcftools=1.16-1
RUN apt-get install -y bedtools=2.30.0+dfsg-3
RUN apt-get install -y python3-pyfaidx=0.7.1-2

## install regtools
RUN curl -L https://github.com/griffithlab/regtools/archive/refs/tags/0.4.2.tar.gz -o regtools-0.4.2.tar.gz
RUN tar xvf regtools-0.4.2.tar.gz && rm regtools-0.4.2.tar.gz
RUN cd regtools-0.4.2 && mkdir build && cd build && cmake ../ && make && cp regtools /usr/bin

## install ScanExitron
RUN curl -L https://github.com/ylab-hi/ScanExitron/archive/refs/tags/v1.1-beta.tar.gz -o ScanExitron-v1.1.tar.gz
RUN tar xvf ScanExitron-v1.1.tar.gz && rm ScanExitron-v1.1.tar.gz
RUN echo 'alias ScanExitron.py="python3 /ScanExitron-1.1-beta/ScanExitron.py"' >> ~/.bashrc
WORKDIR /









