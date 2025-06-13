FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY section_FCSV section_FCSV
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "main3:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]