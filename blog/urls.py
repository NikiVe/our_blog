from django.urls import path
from . views import HomeView, PostCreateView, PostUpdateView, PostDetailView, PostListView, PostDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete')



    
]
