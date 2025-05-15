# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY api/ .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Expose the port Flask runs on
EXPOSE 8000

# Run the Flask app
CMD ["flask", "run"]
