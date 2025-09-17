from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # Allow unauthenticated users to access only login, signup, logout and admin
        if not request.user.is_authenticated and not (
            path.startswith(reverse('home')) or
            path.startswith(reverse('login')) or
            path.startswith(reverse('register')) or
            path.startswith(reverse('logout')) or
            path.startswith(reverse('admin:index'))
        ):
            return redirect('login')
        return self.get_response(request)