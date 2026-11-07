FROM python:3.12-slim
RUN pip install --no-cache-dir 'psycopg[binary]==3.2.9'
WORKDIR /app
COPY server.py /app/server.py
EXPOSE 8000
CMD ["python", "server.py"]
