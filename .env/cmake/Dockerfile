# Dockerfile for CMake C/C++ Development Environment on Ubuntu 22.04
# ---------------------------------------------------------------
# Base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install essential build tools, CMake, and Git
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        ninja-build \
        git \
    && rm -rf /var/lib/apt/lists/*

# Create a workspace directory
WORKDIR /workspace

# Default command: launch a shell
CMD ["bash"]
