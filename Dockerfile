FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

CMD ["uvicorn", "main:main", "--host", "0.0.0.0", "--port", "8000"]
