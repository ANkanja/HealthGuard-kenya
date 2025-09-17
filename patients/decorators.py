from django.shortcuts import redirect
from functools import wraps

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            profile = request.user.profile
            if profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('not_authorized')  # updated
        return wrapper
    return decorator
