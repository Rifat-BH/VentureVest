from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from blogs.models import blogs
from django.shortcuts import redirect

# Create your views here.

def blogDetails(request):
    return render(request,"blogDetails.html")
    
def blogList(request):
    return render(request,"blogList.html") 

def blogPost(request):
    id = request.session['id']
    name = Auts.objects.get(id = id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        en = blogs(user_id_id=id, name=name, title=title,description=details)
        en.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
    # return render(request,"blogList.html") 