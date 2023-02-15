FROM python:3.9-alpine

RUN mkdir /purceddhroxy
WORKDIR /purceddhroxy

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/proxy.py

# Set up a volume for the filters file
VOLUME /filters

CMD ["python", "proxy.py"]
