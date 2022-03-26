FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir python-decouple mysql-connector-python pika scikit-learn

CMD ["python3", "receive.py"]