from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from auths.models import Auts
from .utils import send_otp
from datetime import datetime
import pyotp
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def login(request):

    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        print(user_name)
        userdata = Auts.objects.filter(user_name= user_name).values()
        # print(userdata)
        print(len(userdata))
        for data in userdata:
            if data['password'] == password:
                if data['catagory'] == 'investor' :
                    userid = int(data['id'])
                    cat = data['catagory']
                    user_email = data['email']
                    request.session['email']  = user_email
                    # url = "/investor/home/?id={}".format(userid)
                    send_otp(request)
                    request.session['id']  = userid
                    request.session['catagory']  = cat
                    request.session['email']  = user_email
                    # url = "/investor/home/"  #....
                    return redirect('otp')
                    # return HttpResponseRedirect(url) #....
                    # return HttpResponse("Investor")
                elif data['catagory'] == 'startup':
                    userid = int(data['id'])
                    cat = data['catagory']
                    user_email = data['email']
                    request.session['email']  = user_email
                    send_otp(request)
                    request.session['id']  = userid
                    request.session['catagory']  = cat
                    
                    
                    return redirect('otp')
                    # url = "/startup/home/" #....
                    # return HttpResponseRedirect(url) #....
                    # return HttpResponse("Startup")
                elif data['catagory'] == 'admin':
                    userid = int(data['id'])
                    cat = data['catagory']
                    user_email = data['email']
                    request.session['email']  = user_email

                    send_otp(request)
                    request.session['id']  = userid
                    request.session['catagory']  = cat
                   

                    return redirect('otp')
                    # url = "/adminControl/home/?user_id={}".format(userid) #....
                    # return HttpResponseRedirect(url) #....
                    # url = "/admin/home/?user_id={}".format(userdata.id)
                    # return HttpResponseRedirect(url)
                    # return HttpResponse("Startup")
            else:
                return HttpResponseRedirect("login")

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

            check_user = Auts.objects.filter(user_name= username).values()
            if len(check_user) >= 1:
                return HttpResponseRedirect("/signup/")
            else:
                my_user = Auts(user_name= username, password = password, catagory = catagory, full_name = fullname, email = email)
                my_user.save()

            return HttpResponseRedirect("/login/")
        print(username,password,gender,catagory, email,fullname)
        

    return render(request, "signup.html")

# make sure settings.py has email and pass to get otp
def otp_view(request):
    error_message = None
    if request.method == 'POST':
        otp = request.POST['otp']
        userid = request.session['id']
        cat = request.session['catagory']
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_date = request.session['otp_valid_date']
        
        if otp_secret_key and otp_valid_date is not None:
            valid_until = datetime.fromisoformat(otp_valid_date)
            
            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=60)
                if totp.verify(otp):
                    # useridVerified = get_object_or_404(User, userid=userid)
                    # catagoryVerified = get_object_or_404(User, cat=cat)
                    # login(request, useridVerified, catagoryVerified)
                    
                    if cat == "investor":
                        url = "/investor/home/"  #....
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