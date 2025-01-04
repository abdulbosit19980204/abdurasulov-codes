from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Notification
from .utils import ip_address
from django.utils.translation import gettext as _


class PostListView(generic.ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        ip = ip_address(self.request)
        print("This is queryset ip:", ip)
        d = {}
        d['text'] = _("This is a simple text")
        d['posts'] = Post.objects.all()
        if self.request.user.is_authenticated:
            d['notifications'] = len(Notification.objects.filter(is_read=False, user=self.request.user))
        return d


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'body']
    login_url = 'admin:login'

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
