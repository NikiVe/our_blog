from django.urls import path
from . views import HomeView, PostCreateView, PostUpdateView, PostDetailView, PostListView, PostDeleteView, CommentView, CategoriesView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/', CommentView.as_view(), name='comment'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),



]
