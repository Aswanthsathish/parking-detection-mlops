FROM python:3.10-slim

WORKDIR /app

COPY requirements-docker.txt .

RUN pip install -r requirements-docker.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
