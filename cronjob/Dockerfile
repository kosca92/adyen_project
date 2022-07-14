FROM python:3.9


# Updating the packages and installing cron
RUN apt-get update && apt-get install cron -y && pip install psycopg2

# Crontab file copied to cron.d directory.
COPY cronjob /etc/cron.d/container_cronjob
RUN chmod +x /etc/cron.d/container_cronjob

# Apply cron job
RUN crontab /etc/cron.d/container_cronjob

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Script file copied into container.
COPY script.py ./

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log