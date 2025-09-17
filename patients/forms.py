from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=True)
    location = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'phone_number', 'age', 'gender', 'location']



class UserLoginForm(AuthenticationForm):
    # You can customize labels/placeholders if you like
    pass
