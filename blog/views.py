from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Post
from .forms import PostForm


def index(request):
    post_list = Post.objects.order_by("-pub_date")
    return render(request, "blog/post_list.html", {"post_list": post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse("blog:detail", args=(post.pk,)))
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog:detail", args=(post.pk,)))
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form, "post": post})


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse("blog:index"))
    return render(request, "blog/post_confirm_delete.html", {"post": post})