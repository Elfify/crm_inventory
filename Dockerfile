FROM python:3.11 AS base

WORKDIR /app


# Install system dependencies required for Python, Rust, and general build processes
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
curl \
libpq-dev \
&& rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry==1.7.1
COPY . /app
RUN poetry install

# Set the PATH to include the poetry bin
ENV PATH="${PATH}:/root/.local/bin"

# RUN find ./entrypoints -type f -name "*.sh" -exec chmod +x {} \;

# EXPOSE 8000