from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk': self.object.pk})


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'update.html'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        user = self.request.user
        if user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        user = self.request.user
        if user == post.author:
            return True
        return False
