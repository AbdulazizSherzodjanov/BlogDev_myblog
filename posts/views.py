from django.shortcuts import render
from posts.models import Category, Post


def homepage(request):
    LastPost = Post.objects.all().order_by('-id').first()
    data = Post.objects.all().order_by('-id')[1:7]
    interested_posts = Post.objects.all().order_by('-post_view')[0:8]
    categories = Category.objects.all()
    context = {
        'navbar': categories,
        'LastPost': LastPost,
        'data': data,
        'interested_posts': interested_posts
    }
    return render(request, 'home.html', context)


def post_detail(request, slug):
    categories = Category.objects.all()
    post = Post.objects.get(slug=slug)
    post.post_view = post.post_view + 1
    post.save()
    interested_posts = Post.objects.all().order_by('-post_view')[0:8]
    context = {
        'post': post,
        'interested_posts': interested_posts,
        'navbar': categories,
    }
    return render(request, 'post_detail.html', context)


def allPost(request):
    context = {}
    categories = Category.objects.all()
    interested_posts = Post.objects.all().order_by('-post_view')[0:8]
    context['interested_posts']=interested_posts
    context['navbar']=categories
    data = Post.objects.all()
    context['posts'] = data
    if 'catId' in request.GET:
        catId = request.GET['catId']
        filterData = Post.objects.filter(cat_id=catId)
        context['posts']=filterData
    return render(request, 'allPost.html', context)
    # context = {
    #     'posts': data,
    #     'interested_posts': interested_posts,
    #     'navbar': categories,
    # }




