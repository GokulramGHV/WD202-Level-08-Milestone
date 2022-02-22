from datetime import timedelta

from celery.decorators import periodic_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from task_manager.celery import app

from tasks.models import STATUS_CHOICES, EmailSettings, Task


@periodic_task(run_every=timedelta(seconds=30))
def send_email_remainder():
    print("Starting to process email")
    now = timezone.now()
    for email in EmailSettings.objects.filter(email_enable=True, email_time__lte=now):
        user = User.objects.get(id=email.user.id)
        email_content = "Task Report\nHere's your report for today:\n"
        pending_qs = Task.objects.filter(user=user, completed=False, deleted=False)
        for status in STATUS_CHOICES:
            count = pending_qs.filter(status=status[0]).count()
            email_content += f"{status[0]}: {count}\n"

        email.email_time += timedelta(days=1)
        email.save()

        send_mail(
            "Task Report (Breakdown based on task status)",
            email_content,
            "task_mail@taskmanager.com",
            [user.email],
        )
        print("Completed Processing for User", user.username, user.id)
