from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostCreateForm
from .models import Post


def main(request):
    """Главная страница постов."""

    posts = Post.objects.order_by('-date')[:10]

    context = {
        'posts': posts
    }

    return render(request, 'posts/main.html', context)


def post_detail(request, slug):
    """Страница отдельного поста."""

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    """Страница создания поста."""

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostCreateForm()

    context = {
        'form': form
    }

    return render(request, 'posts/post_create_form.html', context)
