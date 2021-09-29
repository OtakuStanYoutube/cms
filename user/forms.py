from django.forms import EmailField
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
