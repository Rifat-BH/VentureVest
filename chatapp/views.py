from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chatapp.models import MessageDb
from django.db.models import Count
from auths.models import Auts
from django.db.models import Q
# Create your views here.
def home(request):
    id = request.session['id']
    print(id)

    messages = MessageDb.objects.select_related('r_id').filter(r_id=id).values('s_id').annotate(count=Count('s_id')).order_by('-send_date')

    name_list=[]
    for m in messages:
        s_id = m['s_id']
        fname = Auts.objects.filter(id = s_id).values('full_name')
        for i in fname:
            name = i['full_name']
            name_list.append((name,s_id))
    # print(list(messages))
    print(name_list)
    print(name_list[0][1])
    rid = name_list[0][1]

    get_message = MessageDb.objects.filter(Q(s_id = id, r_id =rid) | Q(s_id = rid, r_id =id)).values().order_by('send_date')
    print(get_message)
    data ={
        'rec_name' : name_list
    }
    return render(request,'chat.html',data)