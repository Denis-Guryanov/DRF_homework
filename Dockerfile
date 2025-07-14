FROM python:3.11-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Копируем pyproject.toml, poetry.lock и README.md для установки зависимостей
WORKDIR /code
COPY pyproject.toml poetry.lock README.md ./

# Установка зависимостей проекта (без установки самого пакета)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем остальной код
COPY . .

# Открываем порт для Django
EXPOSE 8000

CMD ["bash"] 