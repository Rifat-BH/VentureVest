from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from startup.models import startupBasicInfo
from backupStartupDB.models import startupBasicInfo2, applyForFundrising, monthlyRevenue, profit

from  investor.models import Invest
from backupStartupDB.models import startupBasicInfo2
from django.db.models import Sum,Count, Q
import math
from datetime import date
# Create your views here.
def startupInfo(request):
    id = request.session['id']
    checkuser= startupBasicInfo2.objects.filter(user_id_id = id).values()
    if request.method == 'POST':
        companyName = request.POST.get('companyName')
        companyAddress = request.POST.get('companyAddress')
        companyDescription = request.POST.get('companyDescription')
        en = startupBasicInfo2(user_id_id=id, companyName=companyName, companyAddress=companyAddress,companyDescription=companyDescription)
        en.save()
        url = "/startup/startupDashboard/?user_id={}".format(id)
        return HttpResponseRedirect(url)
    if len(checkuser)==0:
        return render(request,"startupBasicInfo.html")
    else:
        url = "/startup/startupDashboard/?user_id={}".format(id)
        return HttpResponseRedirect(url)
    #   return render(request,"startupDashboard.html")
  


def applyForFundrisingViews(request):
    # if request.method == 'GET':
    #     id = request.GET.get('user_id')
    id = request.session['id']
    # checkuser= applyForFundrising.objects.filter(user_id_id = id).values()
    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')
        investment = request.POST.get('investment')
        roi = request.POST.get('roi')
        Repayments = request.POST.get('Repayments')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        vat = request.FILES.get('vat')
        bin = request.FILES.get('bin')
        licence = request.FILES.get('licence')
        revenue = request.POST.get('revenue')
        gross_margin = request.POST.get('gross_margin')
        mrr = request.POST.get('mrr')
        cac = request.POST.get('cac')
        burn_rate = request.POST.get('burn_rate')
        
        en = applyForFundrising(user_id_id=id, name=name, duration=duration,investment=investment,roi=roi,Repayments=Repayments,description=description,image=image,vat=vat,bin=bin,licence=licence,revenue=revenue,gross_margin=gross_margin,mrr=mrr,cac=cac,burn_rate=burn_rate,)
        en.save()
        url = "/startup/startupDashboard/?user_id={}".format(id)
        return HttpResponseRedirect(url)
        # return render(request,"startupDashboard.html",data)
        
def monthlyRevenueViews(request):
    id = request.session['id']
    if request.method == 'POST':
        month = request.POST.get('month')
        currentRevenue = request.POST.get('currentRevenue')
        currentProfit = request.POST.get('currentProfit')
        
        en = monthlyRevenue(user_id_id=id, month=month, currentRevenue=currentRevenue,currentProfit=currentProfit)
        en.save()
        url = "/startup/startupDashboard/?user_id={}".format(id)
        return HttpResponseRedirect(url)

def startupDashboard (request):
    id = request.session['id']
    checkuser= applyForFundrising.objects.filter(user_id_id = id).values()
    checkuser2= monthlyRevenue.objects.filter(user_id_id = id).values()
    # print(len(startupData))
    
    if len(checkuser) == 0 and len(checkuser2) == 0:
        startupData =  startupBasicInfo2.objects.get(user_id_id = id)
        data={
        'startupData':startupData,
        }
        return render(request,"startupDashboard.html",data)
    if len(checkuser2) == 0:
        startupData =  startupBasicInfo2.objects.get(user_id_id = id)
        startupData2 =  applyForFundrising.objects.get(user_id_id = id)

        c_name = startupData.companyName
        totalInvest = Invest.objects.filter(company_name = c_name).annotate(c = Count("id")).values("c").annotate(total = Sum("invest_ammount")).values("total")
        print(totalInvest)
        goal = int(startupData2.investment)

        if totalInvest[0]['total'] == None:
            invAm = 0
        else:
            invAm = int(totalInvest[0]['total'])
        procced = (invAm/goal) *100
        data={
            'startupData':startupData,
            'startupData2':startupData2,
            'totalInvest' : invAm,
            'proBar' : procced,
        }
        return render(request,"startupDashboard.html",data)
    else:
        startupData =  startupBasicInfo2.objects.get(user_id_id = id)
        startupData2 =  applyForFundrising.objects.get(user_id_id = id)
        startupData3 =  monthlyRevenue.objects.filter(user_id_id = id)

        c_name = startupData.companyName
        totalInvest = Invest.objects.filter(company_name = c_name).annotate(c = Count("id")).values("c").annotate(total = Sum("invest_ammount")).values("total")
        print(totalInvest)
        goal = int(startupData2.investment)

        if totalInvest[0]['total'] == None:
            invAm = 0
        else:
            invAm = int(totalInvest[0]['total'])
        procced = (invAm/goal) *100
        data={
            'startupData':startupData,
            'startupData2':startupData2,
            'startupData3':startupData3,
            'totalInvest' : invAm,
            'proBar' : procced,
        }
        return render(request,"startupDashboard.html",data)


def startupList (request):
    startupData2 =  applyForFundrising.objects.filter(status =1)
    data ={
        'startupData2' : startupData2
    }
    return render(request,"startupList.html",data)
    # return render(request,"startupList.html")

def search_startup(request):
    if request.method == 'POST':
        search_key = request.POST.get('search')
    if search_key != None:
        startupData2 =  applyForFundrising.objects.filter(Q(status =1, name__icontains = search_key) | Q(status =1, description__icontains = search_key))
    else:
        startupData2 =  applyForFundrising.objects.filter(status =1)
    data ={
        'startupData2' : startupData2
    }
    return render(request,"startupList.html",data)

def startupDetailsViews(request,id):
    uid = request.session['id']
    invAm = 0

    startupData =  startupBasicInfo2.objects.get(user_id_id = id)
    c_name = startupData.companyName
    startupData2 =  applyForFundrising.objects.get(user_id_id = id)
    startupData3 =  monthlyRevenue.objects.filter(user_id_id = id)
    totalInvest = Invest.objects.filter(company_name = c_name).annotate(c = Count("id")).values("c").annotate(total = Sum("invest_ammount")).values("total")
    print(totalInvest)
    goal = int(startupData2.investment)

    if totalInvest[0]['total'] == None:
        invAm = 0
    else:
        invAm = int(totalInvest[0]['total'])
    procced = (invAm/goal) *100
    print(procced)

    data={
        'startupData':startupData,
        'startupData2':startupData2,
        'startupData3':startupData3,
        's_id' : uid,
        'rec_id' : id,
        'totalInvest' : invAm,
        'proBar' : procced,
    }
    return render(request,"startupDetails.html",data)

def funding_details(request):
    id = request.session['id']
    nameQ = startupBasicInfo2.objects.get(user_id_id = id)
    name = nameQ.companyName
    inv_data = Invest.objects.select_related('user_id').filter(company_name = name)
    print(inv_data)
    ln = []
    lid = []
    for n in inv_data:
        na = n.user_id.full_name
        id = n.user_id.id
        lid.append(id)
        ln.append(na)
    
    return JsonResponse({'data' : list(inv_data.values()), 'i_name' : ln, 'i_id' : lid})

def return_profit(request):
    if request.method == 'POST' :
        id = request.POST.get('s_id')
        i_id = request.POST.get('i_id')
        installment = request.POST.get('installment')
        roi = request.POST.get('roi')
        comment = request.POST.get('comment')
    c_idQ = startupBasicInfo2.objects.get(user_id_id = id)
    c_name = c_idQ.companyName
    amQ = Invest.objects.filter(Q(user_id_id = i_id) & Q(company_name = c_name)).annotate(c = Count("id")).values("c").annotate(total_amnt = Sum("invest_ammount")).values("total_amnt")
    roiInt = (int(roi)/100)+1
    installmentInt = int(installment)
    ammount = 0
    for a in amQ:
        ammount += int(a['total_amnt'])
    print(ammount)
    
    pay_ammount = (ammount*roiInt)/installmentInt
    data = {
        'com_id' : i_id,
        'ammount' : math.ceil(pay_ammount),
        'roi' : comment,
    }
    return render(request, 'paymentGatewat.html', data)

def return_profit_save_db(request):
    st_ids = request.session['id']
    if request.method == 'POST':
        comment = request.POST.get('roi')
        inv_id = request.POST.get('com_id') 
        ammount = request.POST.get('amount') 
        print(st_ids)
    sprofit = profit(st_id_id=st_ids, ammount=ammount, inv_id_id=inv_id, comments=comment)
    sprofit.save()
    return HttpResponseRedirect('/startup/home/')