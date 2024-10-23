FROM python:latest

WORKDIR /app

COPY server.py /app/server.py
COPY regression.joblib /app/regression.joblib
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8756"]