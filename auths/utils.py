import pyotp
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings

# make sure settings.py has email and pass to get otp
def send_otp(request):
    user_email = request.session['email']
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = totp.now()
    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)
    
    subject = "VenturVest: Verify Your Account"
    message = f"{otp} This is an one time password. It is valid for 1 minute."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
    
    print(f"your one time password is {otp}")
    

# def send_email_to_client(otp):
#     otp = otp
#     subject = "VenturVest: Verify Your Account"
#     message = f"{otp} This is an one time password. It is valid for 1 minute."
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = ["rsarifat@gmail.com"]
#     send_mail(subject, message, from_email, recipient_list)
    
