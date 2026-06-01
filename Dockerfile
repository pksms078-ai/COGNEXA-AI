Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r backend/requirements.txt

EXPOSE 5000

CMD ["python","backend/app.py"]
deployment/docker-compose.yml
YAML
version: "3.9"

services:

  cognexa:

    build: .

    container_name: cognexa

    ports:

      - "5000:5000"

    restart: always

    environment:

      - ENV=production

    volumes:

      - .:/app
