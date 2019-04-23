from django.conf import settings


def send_mail(user=None, subject=None, message=None):
    user.email_user(subject=subject, message=message)
