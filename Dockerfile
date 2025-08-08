# Parent image
FROM python:3.12-slim

# Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

# Working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy your application code into the container
COPY . .

# run setup.py
RUN pip install --no-cache-dir -e .

# Expose the port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "/app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]