FROM python:3.9-alpine

WORKDIR /purceddhroxy

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "proxy.py"]
