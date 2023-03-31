from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from startup.models import startupBasicInfo


# Create your views here.
def startupInfo(request):
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
        en = startupBasicInfo(name=name, duration=duration,investment=investment,roi=roi,Repayments=Repayments,description=description,image=image,vat=vat,bin=bin,licence=licence,)
        en.save()
        return HttpResponse(request,'startupDashboard.html')
    return render(request,"startupBasicInfo.html")

def startupDashboard (request):
    return render(request,"startupDashboard.html")