# In forms.py
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']


class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']
