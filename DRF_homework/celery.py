import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_homework.settings')

app = Celery('DRF_homework')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'deactivate-inactive-users': {
        'task': 'users.tasks.deactivate_inactive_users',
        'schedule': crontab(hour=0, minute=0),  # Ежедневно в полночь
    },
}