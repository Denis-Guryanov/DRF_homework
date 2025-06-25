FROM python:3.11-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Копируем pyproject.toml и poetry.lock для установки зависимостей
WORKDIR /code
COPY pyproject.toml poetry.lock ./

# Установка зависимостей проекта
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем остальной код
COPY . .

# Открываем порт для Django
EXPOSE 8000

CMD ["bash"] 