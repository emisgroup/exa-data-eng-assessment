FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /data_ingestion .
COPY /data .

CMD ["python", "__init__.py"]
