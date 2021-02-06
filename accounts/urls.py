from django.urls import path
from .views import RegisterView, UserUpdateView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('update/', UserUpdateView.as_view(), name='update user'),
    

]
