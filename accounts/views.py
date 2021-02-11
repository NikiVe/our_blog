from django.shortcuts import render
from django.views import generic as views
from .forms import RegistrationForm, UserUpdateForm, LoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views

from .models import User

from django.contrib.auth import mixins as auth_mixins
# from django.contrib.auth.decorators import login_required



class RegisterView(views.CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class UserUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'registration/user_update.html'
    form_class = UserUpdateForm
    model = User
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None): 
        user = self.request.user 
        return user


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')

    


    




    


    