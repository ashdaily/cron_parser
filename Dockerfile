FROM python:3.11-slim

WORKDIR /deliveroo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PYTHONPATH=/deliveroo/src
ENV LOG_LEVEL=DEBUG

# Default command to run
CMD ["python", "main.py", "*/15 0 1,15 * 1-5 /usr/bin/find"]