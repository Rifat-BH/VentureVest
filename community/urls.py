from django.contrib import admin
from django.urls import path,include
from community import views
urlpatterns = [
    path('posts/', views.posts, name="community-home"),
    path('posts_ajax/', views.posts_ajax, name="community_ajax-home"),
    path('post-details/<post_id>', views.posts_des, name="post_details"),
    path('submit-post/', views.submitPost, name="community-post"),
    path('post-comment/<post_id>/', views.postComment, name="comment-post"),
    path('notification/<user_id>', views.notify, name="notification"),
]