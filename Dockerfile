# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    torch==2.1.0 \
    numpy \
    scipy \
    matplotlib \
    pyprind \
    mat4py \
    joblib

# Copy the application code
COPY . /app

# Default command to run example 1
CMD ["python", "run_example.py", "1"]
