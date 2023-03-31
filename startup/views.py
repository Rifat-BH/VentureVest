from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from startup.models import startupBasicInfo


# Create your views here.
def startupInfo(request):
    # if request.method == 'GET':
    #     id = request.GET.get('user_id')
    id = request.session['id']
    checkuser= startupBasicInfo.objects.filter(user_id_id = id).values()
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
        
        # return HttpResponseRedirect(request,"/startupInfo/")
        en = startupBasicInfo(user_id_id=id, name=name, duration=duration,investment=investment,roi=roi,Repayments=Repayments,description=description,image=image,vat=vat,bin=bin,licence=licence,)
        en.save()
        url = "/startup/startupDashboard/?user_id={}".format(id)
        return HttpResponseRedirect(url)
    if len(checkuser)==0:
        return render(request,"startupBasicInfo.html")
    else:
        url = "/startup/startupDashboard/?user_id={}".format(id)
        return HttpResponseRedirect(url)
    #   return render(request,"startupDashboard.html")
  
def startupDashboard (request):
    id = request.session['id']
    startupData =  startupBasicInfo.objects.get(user_id_id = id)
    data={
        'startupData':startupData
    }
    return render(request,"startupDashboard.html",data)

def startupList (request):
    return render(request,"startupList.html")