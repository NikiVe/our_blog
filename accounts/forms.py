from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import User
from form_mixin.form_mixin import BootstrapFormMixin


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
