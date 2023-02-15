FROM python:3.9

WORKDIR /purceddhroxy

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./purceddhroxy.py" ]