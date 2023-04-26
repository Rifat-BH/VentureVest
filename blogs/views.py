from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from auths.models import Auts
from blogs.models import blogs
from django.shortcuts import redirect

# Create your views here.

def blogDetails(request,id):
    blog = blogs.objects.get(id = id)
    data={
        'blog':blog
    }
    
    return render(request,"blogDetails.html",data)
    
def blogList(request):
    blog =  blogs.objects.all()
    data ={
        'blog' : blog
    }
    return render(request,"blogList.html",data)
    # return render(request,"blogList.html") 

def blogPost(request):
    id = request.session['id']
    name = Auts.objects.get(id = id)
    fname = name.full_name
    
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        image = request.FILES.get('image')
        en = blogs(user_id_id=id, name=fname, title=title,description=details,image=image)
        en.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
    # return render(request,"blogList.html") 