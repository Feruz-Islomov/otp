from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'tel', 'shahar', 'photo', 'password1', 'password2']

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model= User
#         fields = ['username', 'last_name', 'email', 'tel', 'shahar', 'photo']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'tel', 'shahar')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= CustomUser
        fields = ('first_name', 'last_name', 'tel', 'shahar', 'photo')
        