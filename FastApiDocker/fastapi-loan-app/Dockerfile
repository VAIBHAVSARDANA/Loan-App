# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

# Assuming your working directory inside container is /app
COPY loan_model_v2.pkl /app/
COPY scaler.pkl /app/


RUN pip install --no-cache-dir -r requirements.txt

# Copy app code into container
COPY app/ ./app/

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
