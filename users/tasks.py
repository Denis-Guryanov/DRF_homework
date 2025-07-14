from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def deactivate_inactive_users():
    """Деактивирует пользователей, не заходивших более месяца"""
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    count = 0
    for user in inactive_users:
        user.is_active = False
        user.save()
        count += 1

    return f"Деактивировано пользователей: {count}"