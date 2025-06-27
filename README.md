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

## Переменные окружения

Основные переменные уже прописаны в `docker-compose.yaml`:
- `DJANGO_DB_HOST=db`
- `DJANGO_DB_NAME=drf_homework`
- `DJANGO_DB_USER=drf_user`
- `DJANGO_DB_PASSWORD=drf_password`
- `CELERY_BROKER_URL=redis://redis:6379/0`

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

