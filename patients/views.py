from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import UserRegisterForm, UserLoginForm

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = 'login'
    # Allow GET requests for logout (not recommended for production security)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def home_view(request):
    return render(request, 'home.html')
