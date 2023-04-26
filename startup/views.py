from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from startup.models import startupBasicInfo
from backupStartupDB.models import startupBasicInfo2, applyForFundrising, monthlyRevenue
from  investor.models import Invest
from backupStartupDB.models import startupBasicInfo2
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
        data={
            'startupData':startupData,
            'startupData2':startupData2
        }
        return render(request,"startupDashboard.html",data)
    else:
        startupData =  startupBasicInfo2.objects.get(user_id_id = id)
        startupData2 =  applyForFundrising.objects.get(user_id_id = id)
        startupData3 =  monthlyRevenue.objects.filter(user_id_id = id)
        data={
            'startupData':startupData,
            'startupData2':startupData2,
            'startupData3':startupData3
        }
        return render(request,"startupDashboard.html",data)


def startupList (request):
    startupData2 =  applyForFundrising.objects.filter(status =1)
    data ={
        'startupData2' : startupData2
    }
    return render(request,"startupList.html",data)
    # return render(request,"startupList.html")
    
def startupDetailsViews(request,id):
    uid = request.session['id']
    startupData =  startupBasicInfo2.objects.get(user_id_id = id)
    startupData2 =  applyForFundrising.objects.get(user_id_id = id)
    startupData3 =  monthlyRevenue.objects.filter(user_id_id = id)
    data={
        'startupData':startupData,
        'startupData2':startupData2,
        'startupData3':startupData3,
        's_id' : uid,
        'rec_id' : id,
    }
    return render(request,"startupDetails.html",data)

def funding_details(request):
    id = request.session['id']
    nameQ = startupBasicInfo2.objects.get(user_id_id = id)
    name = nameQ.companyName
    inv_data = Invest.objects.select_related('user_id').filter(company_name = name)
    print(inv_data)
    ln = []
    for n in inv_data:
        na = n.user_id.full_name
        ln.append(na)
    
    return JsonResponse({'data' : list(inv_data.values()), 'i_name' : ln})