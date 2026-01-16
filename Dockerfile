# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# Install PyTorch (CPU version) from PyTorch repository
RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --trusted-host download.pytorch.org \
    torch \
    --index-url https://download.pytorch.org/whl/cpu

# Install other Python dependencies from PyPI
RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
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
