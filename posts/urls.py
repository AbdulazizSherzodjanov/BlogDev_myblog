from django.urls import path
from posts.views import homepage, post_detail, allPost

urlpatterns = [
    path('', homepage, name='home-page'),
    path('post_detail/<slug:slug>', post_detail, name='post_detail-page'),
    path('allPost/',allPost,name='allPost-page')
]
