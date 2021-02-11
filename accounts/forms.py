from form_mixin.form_mixin import BootstrapFormMixin
from . models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms





class RegistrationForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'bio', 'profile_picture')


class UserUpdateForm(UserChangeForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    # password = None

    class Meta:
        model = User
        fields = ['email', 'first_name',
                  'last_name', 'bio', 'profile_picture']


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


