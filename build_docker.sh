#!/bin/bash

# -----------------------------------------------------------------------------
# Builds image and upload to a registry
# -----------------------------------------------------------------------------

# Declare variables
BUILDER_NAME="qemubuilder"
QEMU_IMAGE="multiarch/qemu-user-static"
DOCKERFILE="Dockerfile"
CONTEXT="."
REGISTRY_URI="linus.docker:5000"
REPOSITORY_NAME="htcpcp"
BASE_VERSION="0.1.0"
PLATFORM="linux/amd64"
CODEBUILD_BUILD_NUMBER="0"

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --repository_name) REPOSITORY_NAME="$2"; shift ;;
        --base_version) BASE_VERSION="$2"; shift ;;
        --platform) PLATFORM="$2"; shift ;;
        --dockerfile) DOCKERFILE="$2"; shift ;;
        --context) CONTEXT="$2"; shift ;;
        --help) 
        echo "Usage: $0 [options]"
        echo "Options:"
        echo "  --repository_name <repository> Repository name (default: htcpcp)"
        echo "  --base_version <version> Base version tag (default: 0.1.0)"
        echo "  --platform <platform> Platform to build for, comma separated (default: linux/amd64)"
        echo "  --dockerfile <file> Dockerfile to use (default: Dockerfile)"
        echo "  --context <path> Context to use (default: .)"
        exit 0 ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done


echo "Cleaning up"
docker buildx rm $BUILDER_NAME
set -e

echo "Image: $REGISTRY_URI/$REPOSITORY_NAME:$BASE_VERSION"

echo "Setting up Docker Buildx"
docker buildx create --use --name $BUILDER_NAME
docker buildx inspect $BUILDER_NAME --bootstrap

echo "Installing QEMU for multi-architecture support"
docker run --rm --privileged $QEMU_IMAGE --reset -p yes

echo "Building the image for multiple platforms"

# Build in two steps to avoid the error on using insecure registry
docker buildx build --progress=plain --platform $PLATFORM -t $REGISTRY_URI/$REPOSITORY_NAME:$BASE_VERSION -f $DOCKERFILE --output=type=docker $CONTEXT
docker push $REGISTRY_URI/$REPOSITORY_NAME:$BASE_VERSION

echo "Cleaning up"
docker buildx rm $BUILDER_NAME
