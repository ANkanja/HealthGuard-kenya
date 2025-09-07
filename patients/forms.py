from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, initial='patient')
    phone_number = forms.CharField(required=False)
    location = forms.CharField(required=False)
    age = forms.IntegerField(required=False, min_value=0)
    gender = forms.ChoiceField(
        choices=[('', '---------'), ('male', 'Male'), ('female', 'Female')],
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role',
                  'phone_number', 'location', 'age', 'gender']

    def save(self, commit=True):
        # Create the User first
        user = super().save(commit=commit)
        # Ensure email saved on the User
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        # Create/update the linked UserProfile
        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.role = self.cleaned_data.get('role')
        profile.phone_number = self.cleaned_data.get('phone_number')
        profile.location = self.cleaned_data.get('location')
        profile.age = self.cleaned_data.get('age')
        profile.gender = self.cleaned_data.get('gender')
        if commit:
            profile.save()

        return user


class UserLoginForm(AuthenticationForm):
    # You can customize labels/placeholders if you like
    pass
