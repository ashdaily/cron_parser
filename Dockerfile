FROM python:3.11-slim

WORKDIR /cron_parser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PYTHONPATH=/cron_parser/src
ENV LOG_LEVEL=DEBUG

# Default command to run
CMD ["python", "main.py", "*/15 0 1,15 * 1-5 /usr/bin/find"]