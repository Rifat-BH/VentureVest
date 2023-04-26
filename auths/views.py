from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from auths.models import Auts
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
                    request.session['id']  = userid
                    # url = "/investor/home/?id={}".format(userid)
                    url = "/investor/home/"
                    return HttpResponseRedirect(url)
                    # return HttpResponse("Investor")
                elif data['catagory'] == 'startup':
                    userid = int(data['id'])
                    request.session['id']  = userid
                    url = "/startup/home/?user_id={}".format(userid)
                    return HttpResponseRedirect(url)
                    # return HttpResponse("Startup")
                elif data['catagory'] == 'admin':
                    userid = int(data['id'])
                    request.session['id']  = userid
                    url = "/adminControl/home/?user_id={}".format(userid)
                    return HttpResponseRedirect(url)
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

def logout(request):
    del request.session['id']
    return render(request, "login.html")