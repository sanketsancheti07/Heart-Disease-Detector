# app/Dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
CMD ["sh", "-c", "streamlit run --server.port $PORT app.py"]
