from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from auths.models import Auts
from investor.models import Invest
from django.db.models import Count,Sum,Avg
from django.db.models.functions import TruncMonth
from backupStartupDB.models import monthlyRevenue,startupBasicInfo2
from datetime import date
from django.db.models.functions import ExtractMonth
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
    com_list = Invest.objects.filter(user_id = id).annotate(com = Count('company_name')).values('company_name')
    print(com_list)

    data={
        'name' : user_des,
        'inv_data' : inv_data,
        'com_name' : com_list,
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

def investData(request):
    u_id = request.session['id']
    if request.method == "POST":
        ammount = request.POST.get('amount')
        com_id = request.POST.get('com_id')
        roi = request.POST.get('roi')
        today = date.today()
        print(ammount)
        nameQ = startupBasicInfo2.objects.get(user_id_id = com_id)
        com_name = nameQ.companyName
        print(com_name)
        new_investment = Invest(user_id_id = u_id, date = today, company_name = com_name,invest_ammount = ammount,returen_rate =roi)
        new_investment.save()

        url = '/startup/startupDetails/{}'.format(com_id)
        return HttpResponseRedirect(url)

def payment(request):

    if request.method == "POST":
        com_id = request.POST.get('com_id')
        ammount = request.POST.get('ammount')
        roi = request.POST.get('roi')
        data ={
            'com_id' : com_id,
            'ammount' : ammount,
            'roi' : roi,
        }
        return render(request, 'paymentGatewat.html', data)   
def get_data_graph2(request,cname):
    c_idQ = startupBasicInfo2.objects.get(companyName = cname)
    print(c_idQ.user_id_id)
    com_id = c_idQ.user_id_id

    revQ = monthlyRevenue.objects.filter(user_id_id = com_id).annotate(months=ExtractMonth('month')).values('months').annotate(total=Sum('currentRevenue')).values('months','total')
    print(revQ)

    data = {
        'com' : com_id
    }
    
    return render(request, 'revGraph.html', data)

def get_data_graph2_ajax(request,cid):
 
    com_id = cid

    revQ = monthlyRevenue.objects.filter(user_id_id = com_id).annotate(months=ExtractMonth('month')).values('months').annotate(total=Sum('currentRevenue')).values('months','total').order_by("months")
    print(revQ)

    data = {
        'g2_data' : list(revQ)
    }
    
    return JsonResponse(data)