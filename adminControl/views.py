from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from backupStartupDB.models import startupBasicInfo2, applyForFundrising, monthlyRevenue


# Create your views here.
def adminApproval(request):
    approve = applyForFundrising.objects.filter(status = 0)
    data={
        'approve':approve
    }
    return render(request,"admin.html",data)