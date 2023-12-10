FROM tiangolo/uvicorn-gunicorn:python3.10

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./*.py /app/
COPY ./templates /app/templates
COPY ./static /app/static
COPY ./*.ndjson /app/

WORKDIR /app