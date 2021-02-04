from django.shortcuts import render
from django.views import generic as views
from . forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required


class RegistrationView(views.CreateView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


    


    