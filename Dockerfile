# Use Python image
FROM python:3.13-slim

# Set working folder
WORKDIR /app

# Copy all project files
COPY . .

# Install libraries
RUN pip install --no-cache-dir -r requirements.txt

# Open FastAPI port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]