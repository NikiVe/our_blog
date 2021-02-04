from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import User


class RegistrationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name', 'bio', 'profile_picture')


# class MyUserChangeForm(UserChangeForm):

#     class Meta(MyUserChangeForm):
#         model = User
#         fields = ('email', 'first_name', 'last_name', 'bio', 'profile_picture')