FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3-pip ffmpeg libgl1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]