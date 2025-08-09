FROM python:3.11-slim

WORKDIR /app

# system libs for numpy pandas scipy scikit learn lightgbm
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    libgomp1 \
    cmake \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.api.txt .
RUN pip install --no-cache-dir -r requirements.api.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]