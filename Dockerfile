# Use Python 3.11-slim as the base image
FROM python:3.11-slim

# Install Redis and necessary build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose Redis default port
EXPOSE 6379

# Add python code
RUN pip install redis grpcio grpcio-tools

RUN mkdir -p "/apps"

COPY . /apps

WORKDIR /apps


# Start both Python and Redis
CMD ["redis-server", "--daemonize", "no"]