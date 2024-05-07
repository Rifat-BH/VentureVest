from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from auths.models import Auts
from .utils import send_otp
from datetime import datetime
import pyotp
from django.conf import settings
from django.core.mail import send_mail

import bcrypt
# Create your views here.

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        
        userdata = Auts.objects.filter(user_name=user_name).first()  # Using first() instead of values()
        
        if userdata:
            stored_password = userdata.password  # Fetch the hashed password from the database
            print(stored_password, password.encode('utf-8'))
            # Verify the password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                userid = int(userdata.id)
                cat = str(userdata.catagory)
                user_email = userdata.email
                request.session['id'] = userid
                request.session['catagory'] = cat
                hashed_cat = bcrypt.hashpw(cat.encode('utf-8'), bcrypt.gensalt())
                request.session['hsq'] = hashed_cat.decode('utf-8')
                request.session['email']  = user_email
                if cat == 'investor':
                    send_otp(request)
                    return HttpResponseRedirect('/otp/')
                elif cat == 'startup':
                    send_otp(request)
                    return redirect('otp')
                elif cat == 'admin':
                    send_otp(request)
                    return redirect('otp')
            else:
                # Passwords don't match
                return redirect('login/')

        else:
            # User does not exist
            return HttpResponseRedirect("/login/")

    return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_pas = request.POST.get('c_pass')
        gender = request.POST.get('gender')
        catagory = request.POST.get('catagory')
        fullname = fname + " " + lname
        if password == c_pas:
            hash_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            check_user = Auts.objects.filter(user_name= username).values()
            if len(check_user) >= 1:
                return HttpResponseRedirect("/signup/")
            else:
                my_user = Auts(user_name= username, password = hash_password.decode('utf-8'), catagory = catagory, full_name = fullname, email = email)
                my_user.save()

            return HttpResponseRedirect("/login/")
        print(username,password,gender,catagory, email,fullname)
        

    return render(request, "signup.html")

# make sure settings.py has email and pass to get otp
def otp_view(request):
    error_message = None
    if request.method == 'POST':
        otp = request.POST['otp']
        # otp_secret_key = request.session['otp_secret_key']
        # otp_valid_date = request.session['otp_valid_date']
        # totp = pyotp.TOTP(otp_secret_key, interval=120)
        # print(totp.verify(otp), request.session['catagory'],request.session['otp_valid_date'], datetime.now())
        userid = request.session['id']
        cat = request.session['catagory']
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_date = request.session['otp_valid_date']
        
        if otp_secret_key and otp_valid_date is not None:
            valid_until = datetime.fromisoformat(otp_valid_date)
            
            if valid_until > datetime.now() :
                totp = pyotp.TOTP(otp_secret_key, interval=60)
                if totp.verify(otp):
                    # useridVerified = get_object_or_404(User, userid=userid)
                    # catagoryVerified = get_object_or_404(User, cat=cat)
                    # login(request, useridVerified, catagoryVerified)
                    print("success")
                    if bcrypt.checkpw(cat.encode('utf-8'), request.session['hsq'].encode('utf-8')) or cat == "investor":
                        url = "/investor/home/"  #....
                        print("user e-mail:{} user login through {}".format(request.session['email'], request.META.get('HTTP_REFERER')))
                    if cat == "startup":
                        url = "/startup/home/" #....
                    if cat == "admin":
                        url = "/adminControl/home/?user_id={}".format(userid)
                    
                
                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']
                    
                    return HttpResponseRedirect(url) #....

                    # return redirect('login')
                else:
                    error_message = 'invalid one time password'
            else:
                error_message = 'one time password has expired'
        else:
            error_message = 'ups...something went wrong :('
                 
        
    return render(request, 'otp.html', {'error_message': error_message} )


def logout(request):
    del request.session['id']
    del request.session['catagory']
    return render(request, "login.html")