from django.shortcuts import render
from django.views import generic as views
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixins


class HomeView(views.TemplateView):
    template_name = 'index.html'


class PostCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)


class PostDetailView(views.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('home')

class PostListView(views.ListView):
    model = Post
    template_name = 'post_list.html'
    # context_object_name = post

class PostDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

 
