from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import PostForm
from .models import Post


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