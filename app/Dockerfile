# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /restaurant-api

# Copy requirements and install them
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py and core module
COPY api/app.py .
COPY api/core ./core

# Expose Flask port
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]
