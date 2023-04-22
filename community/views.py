from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from community.models import CommunityPost, CommunityComment, CommentNofity
from auths.models import Auts
from django.db.models import Q
# Create your views here.
def posts(request):
    user_id = request.session['id']
    all_posts = CommunityPost.objects.select_related('post_by').all().order_by('-post_date')
    print(all_posts)
    # for a in all_posts:
    #     print(a.post_by.full_name)
    data ={
        'user_id' : user_id,
        'posts' : all_posts.values()
    }
    return render(request,"community.html",data)
    # return JsonResponse({'all_post': list(all_posts.values())})

def posts_ajax(request):
    all_posts = CommunityPost.objects.select_related('post_by').all().order_by('-post_date')
    print(all_posts)
    post_by_full_name = []
    for a in all_posts:
        # print(a.post_by.full_name)
        post_by_full_name.append(a.post_by.full_name)
    data ={
        'posts' : all_posts.values()
    }
    # return render(request,"community.html",data)
    return JsonResponse({'all_post': list(all_posts.values()), 'post_by_name' : list(all_posts.values('post_by__full_name')) })

def posts_des(request,post_id):
    post_ditls = CommunityPost.objects.get(id = post_id)
    # print(post_ditls)
    all_comment = CommunityComment.objects.filter(post_id = post_id).order_by("-comment_date")
    # print(all_comment)
    post_data ={
        'post' : post_ditls,
        'comment' : all_comment,
    }
    return render(request,"post_details.html",post_data)

def submitPost(request):
    user_id = request.session['id']
    if request.method == "POST":
        post_title = request.POST.get('post_title')
        post_des = request.POST.get('post_details')
        query = CommunityPost(post_by_id = user_id, post_title = post_title, post_des = post_des)
        query.save()
        return HttpResponse("Submit")
    
def postComment(request,post_id):
    user_id = request.session['id']
    name = Auts.objects.get(id = user_id)
    fname = name.full_name
    post_by = CommunityPost.objects.get(id = post_id)
    p_by = post_by.post_by.id
    print(fname,p_by)
    if request.method == "POST":
        cmnt = request.POST.get('comment')
        new_comment = CommunityComment(post_id_id = post_id, comment_by_id = user_id, comment = cmnt)
        new_comment.save()
        n_text = fname + " Comment on your post"
        add_notifi = CommentNofity(post_id = post_id, comment_by_id = user_id, notify = n_text, post_by_id = p_by)
        add_notifi.save()
        url = "/community/post-details/{}".format(post_id)
        return HttpResponseRedirect(url)
    
def notify(request,user_id):
    get_notifi = CommentNofity.objects.filter(Q(post_by_id = user_id) & Q(status=0)).values()
    count_n = len(get_notifi)

    set_seen = CommentNofity.objects.filter(post_by_id = user_id).update(status = 1)
    return JsonResponse({'notif_data' : list(get_notifi), 'count' : count_n})