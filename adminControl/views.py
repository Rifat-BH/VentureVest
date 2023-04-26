from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from django.shortcuts import redirect
from backupStartupDB.models import startupBasicInfo2, applyForFundrising, monthlyRevenue


# Create your views here.
def adminDetails(request):
    approve = applyForFundrising.objects.filter(status = 0)
    data={
        'approve':approve
    }
    return render(request,"admin.html",data)

def adminApproval(request,id):
    applyForFundrising.objects.filter(user_id_id = id).update(status = 1)
        # return render(request,"admin.html")
    return redirect(request.META.get('HTTP_REFERER'))

def adminDeny(request,id):
    applyForFundrising.objects.filter(user_id_id = id).delete()
    return redirect(request.META.get('HTTP_REFERER'))
