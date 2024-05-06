# signals.py

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_logged_in(sender, request, user, **kwargs):
    # Log the successful login event
    print(f"User {user.username} logged in. Referer: {request.META.get('HTTP_REFERER')}")

@receiver(user_logged_out)
def log_user_logged_out(sender, request, user, **kwargs):
    # Log the logout event
    print(f"User {user.username} logged out.")

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    # Log the failed login attempt
    print(f"Login failed for username {credentials['username']}. Referer: {request.META.get('HTTP_REFERER')}")
