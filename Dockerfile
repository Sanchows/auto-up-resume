FROM python:3.12.2-slim-bullseye
RUN apt update && apt install -y \
    cron \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . ./
RUN chmod +x /app/cron-entrypoint.sh
RUN echo "51 * * * * /app/cron-entrypoint.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/my-cron-job
RUN chmod 0644 /etc/cron.d/my-cron-job
RUN crontab /etc/cron.d/my-cron-job
CMD ["/bin/sh", "-c", "cron && touch /var/log/cron.log && tail -f /var/log/cron.log"]
