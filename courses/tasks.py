from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Course
from users.models import Subscription
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_course_update_notification(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course)

    for subscription in subscriptions:
        subject = f'Обновление курса {course.name}'
        message = f'Курс "{course.name}" был обновлен. Проверьте новые материалы!'
        recipient_list = [subscription.user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)