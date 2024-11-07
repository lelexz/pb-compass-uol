FROM python:3-slim

WORKDIR /app

RUN pip install boto3

COPY . /app/

CMD ["python", "csvload.py"]

