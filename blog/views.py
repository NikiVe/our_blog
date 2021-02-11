from django.shortcuts import render, redirect
from django.views import generic as views
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
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
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context[self.context_object_name]
        context['form'] = CommentForm()
        context['comments'] = post.comment_set.all().order_by('-id')

        return context


class PostUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('home')
    


class PostListView(views.ListView):
    model = Post
    template_name = 'post_list.html'
    # context_object_name = post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')

        return context


class PostDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class CommentView(auth_mixins.LoginRequiredMixin, views.FormView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('post-detail', self.kwargs['pk'])


class CategoriesView(views.ListView):
    model = Category
    template_name = 'categories_list.html'


class CategoryView(views.DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context[self.context_object_name]
        context['posts'] = category.post_set.all().order_by('-id')

        return context
