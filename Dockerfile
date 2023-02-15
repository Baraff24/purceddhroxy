FROM python:3.9-alpine

WORKDIR /purceddhroxy

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "proxy.py", "-d", "${DESTINATION_HOST}", "-p", "${DESTINATION_PORT}"]
