from django.shortcuts import render
from django.http import HttpResponse
from auths.models import Auts
# Create your views here.
def home(request):
    # profile = Auts.objects.filter(id = investor_id).values()
    # print(profile)
    if request.method == 'GET':
        i_id = request.GET.get('id')

    return render(request,"investor.html", {'uid' : i_id})