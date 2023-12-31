FROM ubuntu:20.04 as base

# Config
ARG BRANCH="master"
ARG CLANG_VERSION=15

# General dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -yq wget gnupg \
 && rm -rf /var/lib/apt/lists/*

# Separately download and add the llvm gpg key
RUN wget https://apt.llvm.org/llvm-snapshot.gpg.key
RUN apt-key add llvm-snapshot.gpg.key
RUN rm llvm-snapshot.gpg.key

# Add the llvm repo to sources
RUN echo "deb http://apt.llvm.org/focal/ llvm-toolchain-focal-${CLANG_VERSION} main" >> /etc/apt/sources.list


# Run dependencies
RUN apt-get update \
 && apt-get install -yq "clang-${CLANG_VERSION}" \
 && rm -rf /var/lib/apt/lists/*


# Build binder
FROM base as build

# Build dependencies
RUN apt-get update
RUN apt-get install -yq \
	"libclang-${CLANG_VERSION}-dev" \
	cmake \
	git \
    build-essential \
    zlib1g-dev \
    libhts-dev \
    libssl-dev

# Clone binder source
ARG REPO="https://github.com/RosettaCommons/binder.git"
RUN git clone --depth 1 --branch "${BRANCH}" "${REPO}" /binder

# Build
WORKDIR "/build"
RUN cmake \
	-DCMAKE_CXX_COMPILER="$(which clang++-"${CLANG_VERSION}")" \
	-DBINDER_ENABLE_TEST=OFF \
	/binder
RUN make "-j$(nproc)"
RUN make install


# Install image
FROM base as install
COPY --from=build /usr/local/bin/binder /usr/local/bin/binder
