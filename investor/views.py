from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from auths.models import Auts
from investor.models import Invest
from django.db.models import Count,Sum,Avg
from django.db.models.functions import TruncMonth
# Create your views here.
def home(request):
    # profile = Auts.objects.filter(id = investor_id).values()
    # print(profile)
    id = request.session['id']
    print(id)

    # i_id = request.GET.get('id')
    user_des = Auts.objects.get(id=id)
    inv_data = Invest.objects.filter(user_id = id).annotate(co=Count('user_id')).values("co").annotate(total_am=Sum('invest_ammount'), avg_ret=Avg('returen_rate')).values('co', 'total_am', 'avg_ret')
    print(inv_data)
    data={
        'name' : user_des,
        'inv_data' : inv_data
    }
    return render(request,"investor.html", data)
def get_data_table(request):
    # i_id = request.GET.get('id')
    id = request.session['id']
    inv_data = Invest.objects.filter(user_id = id)

    return JsonResponse({"t_data" :list(inv_data.values())})
def get_data_graph1(request):
    # i_id = request.GET.get('id')
    id = request.session['id']
    g_data = Invest.objects.filter(user_id = id).annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('invest_ammount')).values('month','total') 
    return JsonResponse({'g_data' : list(g_data)})