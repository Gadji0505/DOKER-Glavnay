# Первый этап: сборка
FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY your_terminal_code.py .

# Второй этап: минимальный образ
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /app/your_terminal_code.py .
COPY --from=builder /app/requirements.txt .

CMD ["python", "your_terminal_code.py"]

