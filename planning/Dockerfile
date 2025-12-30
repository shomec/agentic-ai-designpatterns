FROM python:3.11-slim

WORKDIR /planning

COPY . .

# Install Docker CLI and mcp library
RUN apt-get update && apt-get install -y docker.io && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir mcp

ENTRYPOINT ["python3", "main.py"]
