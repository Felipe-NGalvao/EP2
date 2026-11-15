from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Post


def index(request):
    post_list = Post.objects.order_by("-pub_date")
    return render(request, "blog/post_list.html", {"post_list": post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def create(request):
    if request.method == "POST":
        post = Post(title=request.POST["title"], content=request.POST["content"])
        post.save()
        return HttpResponseRedirect(reverse("blog:detail", args=(post.pk,)))
    return render(request, "blog/post_form.html")


def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return HttpResponseRedirect(reverse("blog:detail", args=(post.pk,)))
    return render(request, "blog/post_form.html", {"post": post})


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse("blog:index"))
    return render(request, "blog/post_confirm_delete.html", {"post": post})