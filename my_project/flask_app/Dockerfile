# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем необходимые пакеты для сборки psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем основной файл приложения
COPY app.py app.py

# Указываем команду по умолчанию для запуска приложения (если необходимо)
# CMD ["python", "app.py"]

