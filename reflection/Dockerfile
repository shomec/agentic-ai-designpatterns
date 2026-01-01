FROM python:3.11-slim

WORKDIR /reflection
ENV PYTHONUNBUFFERED=1

# No external dependencies currently, but good practice to have requirements.txt support
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
