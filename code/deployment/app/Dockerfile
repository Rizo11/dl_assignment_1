# Use Python slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir streamlit requests pandas numpy

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
