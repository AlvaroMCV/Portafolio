from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/post_list.html',{
        'posts': posts
    })
    
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form,
    })

@login_required
#@permission_required(perm='blog.add_comment', raise_exception=True)
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form,
    })

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/new_post.html', 
                  {'form': form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)


    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'post': post,
    })

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.has_perm('blog.delete_post') or request.user == post.autor:
        post.delete()
        messages.success(request, f'El post "{post.titulo}" ha sido eliminado correctamente.')
        return redirect('post_list')
    else:
        messages.error(request, 'No tienes permiso para eliminar este post.')
        return redirect('post_list')