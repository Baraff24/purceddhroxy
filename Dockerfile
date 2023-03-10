FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends tcpdump iptables python3-dev build-essential libpq-dev libnetfilter-queue-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

WORKDIR /app
COPY . .

ENV PYTHONPATH /app

RUN chmod +x ./commands/starter.sh
RUN chmod +x ./commands/iptablesSetup.sh
CMD ["sh", "./commands/starter.sh"]
CMD ["sh", "./commands/iptablesSetup.sh"]
