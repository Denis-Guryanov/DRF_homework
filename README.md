# DRF_homework

## Описание

Этот проект — учебное приложение на Django + Django REST Framework с поддержкой асинхронных задач через Celery, PostgreSQL и Redis. Проект контейнеризирован с помощью Docker и Docker Compose для удобного запуска всех сервисов одной командой.

## Состав
- Django + DRF (основное API-приложение)
- Celery (асинхронные задачи)
- Celery Beat (планировщик задач)
- PostgreSQL (база данных)
- Redis (брокер сообщений для Celery)

## Быстрый старт

### 1. Клонируйте репозиторий
```bash
git clone <адрес-репозитория>
cd DRF_hpmework
```

### 2. Запустите проект через Docker Compose
```bash
docker-compose up --build
```

- Django будет доступен на [http://localhost:8000](http://localhost:8000)
- PostgreSQL — на порту 5432
- Redis — на порту 6379

### 3. Остановка
```bash
docker-compose down
```

## Настройка удаленного сервера для деплоя

1. Установите Docker и docker-compose:
   ```bash
   sudo apt update && sudo apt install -y docker.io docker-compose
   sudo usermod -aG docker $USER
   # Перезайдите в систему или выполните: newgrp docker
   ```
2. Откройте только нужные порты (обычно 22, 80, 443, 8000) и настройте firewall.
3. Создайте пользователя для деплоя и настройте SSH-ключи (без пароля):
   ```bash
   ssh-keygen -t ed25519
   # Добавьте публичный ключ в ~/.ssh/authorized_keys на сервере
   ```
4. Клонируйте репозиторий на сервер или используйте автоматический деплой через GitHub Actions.
5. Убедитесь, что в корне проекта есть файл .env (см. .env.sample).

## CI/CD через GitHub Actions

- Workflow находится в `.github/workflows/ci.yml`.
- Запускается при каждом push/pull_request в ветки develop, main, master.
- Шаги:
  1. Установка зависимостей через poetry
  2. Применение миграций и запуск тестов на sqlite3
  3. Если тесты прошли — деплой на сервер через SSH и запуск docker-compose up -d --build
- Все чувствительные данные (адрес сервера, пользователь, ssh-ключ, путь) хранятся в GitHub Secrets:
  - `SERVER_HOST` — IP или домен сервера
  - `SERVER_USER` — пользователь для SSH
  - `SERVER_SSH_KEY` — приватный ключ (без пароля)
  - `SERVER_PORT` — порт SSH (обычно 22)
  - `SERVER_PATH` — путь до папки с проектом на сервере

## Переменные окружения

- Все переменные для работы приложения описаны в `.env.sample`.
- Сам файл `.env` не должен попадать в git (см. .gitignore).
- Пример:
  ```
  DEBUG=0
  DJANGO_SECRET_KEY=your-secret-key
  DJANGO_DB_HOST=db
  DJANGO_DB_NAME=drf_homework
  DJANGO_DB_USER=drf_user
  DJANGO_DB_PASSWORD=drf_password
  CELERY_BROKER_URL=redis://redis:6379/0
  ```

## Запуск workflow и деплой

1. Сделайте push в ветку develop (или main/master).
2. Убедитесь, что все secrets добавлены в настройках репозитория.
3. После успешных тестов проект автоматически деплоится на сервер и перезапускается через Docker Compose.

---

Если используете Supervisor или Systemd вместо Docker, настройте отдельные сервисы для gunicorn и celery.

## Основные команды

- Применить миграции:
  ```bash
  docker-compose run --rm web python manage.py migrate
  ```
- Создать суперпользователя:
  ```bash
  docker-compose run --rm web python manage.py createsuperuser
  ```
- Запустить тесты:
  ```bash
  docker-compose run --rm web python manage.py test
  ```

## Структура проекта
- `courses/` — приложение с курсами
- `users/` — приложение с пользователями и платежами
- `DRF_homework/` — настройки проекта

## Разработка
- Все зависимости управляются через Poetry (`pyproject.toml`).
- Для локальной разработки можно использовать стандартные команды Django и Celery внутри контейнера `web`.

