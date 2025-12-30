FROM python:3.9-slim

WORKDIR /reflection

# No external dependencies currently, but good practice to have requirements.txt support
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
