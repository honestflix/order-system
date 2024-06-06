FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:main", "--host", "0.0.0.0", "--port", "8000"]
