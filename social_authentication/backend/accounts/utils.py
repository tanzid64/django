import random
from django.core.mail import EmailMessage
from accounts.models import User, OneTimePassword
from django.conf import settings

def generateOtp():
  otp = ""
  for i in range(6):
    otp += str(random.randint(0,9))

  return otp

def send_otp_to_user(email):
  subject = "One Time Passcode for Email Verification"
  otp_code = generateOtp()
  try:
    user = User.objects.get(email=email)
  except User.DoesNotExist:
    return False
  current_site = "myAuth.com"
  email_body = f"Hi {user.first_name} thanks for signing up on {current_site}, please verify your email with the \n one time passcode {otp_code}"
  from_email = settings.DEFAULT_FROM_EMAIL
  OneTimePassword.objects.create(user=user, code=otp_code)
  d_email = EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[email])
  d_email.send(fail_silently=True)

def send_normal_email(data):
  email = EmailMessage(
    subject=data['subject'],
    body=data['body'],
    from_email=settings.EMAIL_HOST_USER,
    to=(data['to'],)
  )
  email.send()
