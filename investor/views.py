from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from auths.models import Auts
from investor.models import Invest
from django.db.models import Count
from django.db.models.functions import TruncMonth
# Create your views here.
def home(request):
    # profile = Auts.objects.filter(id = investor_id).values()
    # print(profile)
    
    if request.method == 'GET':
        i_id = request.GET.get('id')
        user_des = Auts.objects.get(id=i_id)
        inv_data = Invest.objects.filter(user_id = i_id).values()
        print(inv_data)
    data={
        'name' : user_des,
        'inv_data' : inv_data
    }
    return render(request,"investor.html", data)
def get_data_table(request):
    i_id = request.GET.get('id')
    inv_data = Invest.objects.filter(user_id = i_id)

    return JsonResponse({"t_data" :list(inv_data.values())})
def get_data_graph1(request):
    i_id = request.GET.get('id')