FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10.12

COPY ./app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
