from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import PostForm, CommentForm
from .models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


class PostListView(generic.ListView):
    model = Post


class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse("blog:detail", args=(self.object.pk,))


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse("blog:detail", args=(self.object.pk,))


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")


def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog:detail", args=(post.pk,)))
    else:
        form = CommentForm()
    return render(request, "blog/comment_form.html", {"form": form, "post": post})