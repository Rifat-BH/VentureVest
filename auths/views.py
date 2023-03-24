from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    # return HttpResponse("Hi")
    return render(request, "login.html")
