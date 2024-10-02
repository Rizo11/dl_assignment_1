# Use Python slim image for smaller size
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Copy model and any other needed files
COPY ../../models/model.pkl /app/models/model.pkl

# Install Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn pandas numpy scikit-learn joblib pydantic

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the API using Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
