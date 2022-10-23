FROM python:3.9-slim
# FROM text_ocr:1.0

WORKDIR /ocr

COPY . /ocr

RUN apt-get update -q \
    && apt-get clean \
    && apt-get install ffmpeg libsm6 libxext6  -y \
    && apt-get install --no-install-recommends --yes build-essential \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt --no-cache-dir \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]