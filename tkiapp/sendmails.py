from django.conf import settings
from django.core.mail import send_mail

def send_otp(email,first_name,activation_url):
    try:
        subject="your account need to verify"
        message=f'Hi User... your OTP to activate account is -  {activation_url}'
        email_from=settings.EMAIL_HOST
        send_mail(subject,message,email_from,[email])
        return True
    except Exception as e:
        print(e)

def send_notification_on_email(email,subject,message):
    try:
        subject=f"{subject}"
        message=f'{message}'
        email_from=settings.EMAIL_HOST
        send_mail(subject,message,email_from,[email])
        return True
    except Exception as e:
        print(e)