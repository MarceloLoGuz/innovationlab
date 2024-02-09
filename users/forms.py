from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import MyAbsUser


class UsersForm(forms.ModelForm):
    class Meta:
        model = MyAbsUser
        fields = ('name','first_name','last_name','email','phone', 'age')