from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.utils import timezone
from user_cabinet.forms import CommentForm
from .models import Post, Comment


from django.shortcuts import get_list_or_404, get_object_or_404


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context = {
        'posts': contacts,

    }
    return render(request, 'index.html', context=context)


def getfull(request, id):
    form = CommentForm()
    context = {
    'com': form
    }
    # если поста не нет, выкинет исключение
    post = Post.objects.get(id=id)

    context['post'] = post
    context['comments'] = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.data = timezone.now()
            form.post = post
            form.save()

    else:
        form = PostForm()

    return render(request, 'post.html', context=context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'red.html', {'form': form})


def comment(request):
    
    context = {
        'commets': Comment.objects.filter(article_for=id),
        
    }
    return render(request, 'post.html', context=context)
