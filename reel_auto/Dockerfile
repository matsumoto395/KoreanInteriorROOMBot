FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y ffmpeg git && \
    pip install --no-cache-dir -r requirements.txt
COPY app/ ./app
ENV PYTHONUNBUFFERED=1
CMD ["python", "app/main.py"]
