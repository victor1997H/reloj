FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cambiado a 5001 para que coincida con tu app.py
EXPOSE 5001

CMD ["python", "app.py"]