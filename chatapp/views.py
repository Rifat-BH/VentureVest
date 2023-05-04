from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chatapp.models import MessageDb, MessageNofity
from django.db.models import Count
from auths.models import Auts
from django.db.models import Q
# Create your views here.
def home(request):
    id = request.session['id']
    print(id)

    messages = MessageDb.objects.filter(r_id=id).values('s_id').annotate(count=Count('s_id'))
    print(messages.values())
    if len(messages.values()) > 0:
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
        rname= name_list[0][0]

        get_message = MessageDb.objects.filter(Q(s_id = id, r_id =rid) | Q(s_id = rid, r_id =id)).values().order_by('send_date')
        # print(get_message)
        msg_notification = MessageNofity.objects.filter(user_id_id = id).values()
        count_not = MessageNofity.objects.filter(Q(user_id_id = id) & Q(status = 0)).values()
        cNot = len(count_not)
        data ={
            'msgNotif' : msg_notification, 
            'rec_name' : name_list,
            'rec_id' : rid,
            'r_name' : rname,
            's_id' : id,
        }
        
        return render(request,'chat.html',data)
    else:
        return render(request, 'chatNotFound.html')

def get_message(request,rec_id):
    id = request.session['id']
    print(id)

    messages = MessageDb.objects.filter(r_id=id).values('s_id').annotate(count=Count('s_id'))
    print(messages)
    name_lists=[]
    for m in messages:
        s_id = m['s_id']
        fname = Auts.objects.filter(id = s_id).values('full_name')
        for i in fname:
            name = i['full_name']
            name_lists.append((name,s_id))
    print(list(messages))
    print(name_lists)
    rid = rec_id

    get_message = MessageDb.objects.filter(Q(s_id = id, r_id =rid) | Q(s_id = rid, r_id =id)).values().order_by('send_date')
    # print(get_message)
    name = Auts.objects.get(id = rid)
    fullname = name.full_name
    data ={
        'rec_name' : name_lists,
        'rec_id' : rid,
        's_id' : id,
        'r_name' : fullname,
    }
    # return JsonResponse({"msg_data" : list(get_message)})
    return render(request,'chat.html',data)

def get_messages(request,rec_id):
    id = request.session['id']
    print(id)

    messages = MessageDb.objects.select_related('r_id').filter(r_id=id).values('s_id').annotate(count=Count('s_id')).order_by('-send_date')
    print(messages)
    name_list=[]
    for m in messages:
        s_id = m['s_id']
        fname = Auts.objects.filter(id = s_id).values('full_name')
        for i in fname:
            name = i['full_name']
            name_list.append((name,s_id))
    # print(list(messages))
    # print(name_list)
    rid = rec_id

    get_message = MessageDb.objects.filter(Q(s_id = id, r_id =rid) | Q(s_id = rid, r_id =id)).values().order_by('id')
    # print(get_message)
    name = Auts.objects.get(id = rid)
    fullname = name.full_name
    # print(fullname)
    get_notifi = MessageNofity.objects.filter(Q(user_id_id = id) & Q(status=0)).values()
    count_n = len(get_notifi) 
    data ={
        'rec_name' : name_list,
        'rec_id' : rid,
        's_id' : id,
        'r_name' : fullname,
    }
    return JsonResponse({"msg_data" : list(get_message), 'count' : count_n})


def send_message(request):
    if request.method == "POST":
        sender = request.POST.get('s_id')
        receiver = request.POST.get('rec_id')
        mesg = request.POST.get('message')
        print(mesg)
        new_msg = MessageDb(s_id_id = sender, r_id_id=receiver, msgg = mesg)
        new_msg.save()
        name = Auts.objects.get(id = sender)
        f_name = name.full_name
        notext = f_name + "send you a new message"
        new_notifi = MessageNofity(msg_send_by = sender, notify = notext, user_id_id= receiver)
        new_notifi.save()
        return HttpResponse("Send")
    
def send_message_details(request):
    if request.method == "POST":
        sender = request.POST.get('s_id')
        receiver = request.POST.get('rec_id')
        mesg = request.POST.get('message')
        print(mesg)
        new_msg = MessageDb(s_id_id = sender, r_id_id=receiver, msgg = mesg)
        new_msg.save()
        return redirect(request.META.get('HTTP_REFERER'))

def chat_notification(request,id):
    get_notifi = MessageNofity.objects.filter(user_id_id = id).values()
    count_n = len(get_notifi) 
    seen = MessageNofity.objects.filter(user_id_id = id).update(status =1)
    print(get_notifi)
    # print(get_notifi)
    # return JsonResponse({'notif_data' : get_notifi, 'count' : count_n})
    data = {
        'notif_data' : list(get_notifi),
        'count' : count_n
    }
    return JsonResponse(data)