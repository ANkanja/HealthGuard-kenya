from django.contrib import messages  # Fix the import
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import MedicalHistory, UserProfile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import role_required

from .forms import UserRegisterForm, UserLoginForm

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Update the profile created by the signal instead of creating new one
            profile = user.profile  # This exists because of the signal
            profile.phone_number = form.cleaned_data.get('phone_number')
            profile.age = form.cleaned_data.get('age')
            profile.gender = form.cleaned_data.get('gender')
            profile.location = form.cleaned_data.get('location')
            profile.save()
            
            messages.success(request, 'Your account has been created successfully!')
            login(request, user)  # Auto login after registration
            
            # Redirect based on role
            if profile.role == "patient":
                return redirect('patient_dashboard')
            elif profile.role == "clinic_staff":
                return redirect('clinic_staff_dashboard')
            elif profile.role == "doctor":
                return redirect('doctor_dashboard')
            elif profile.role == "gov_official":
                return redirect('gov_dashboard')
            elif profile.role == "chw":
                return redirect('chw_dashboard')
        # If form is invalid, fall through to render the form with errors
    else:
        # GET request - show empty form
        form = UserRegisterForm()
    
    # This handles both GET requests and POST requests with invalid forms
    return render(request, 'register.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        # Redirect everyone to home after login
        return reverse('home')


class UserLogoutView(LogoutView):
    next_page = 'login'
    # Allow GET requests for logout (not recommended for production security)
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



def home_view(request):
    # Static content for now, can later fetch from DB or API
    context = {
        "about": "HealthGuard Kenya is a platform designed to connect patients, doctors, clinics, and community health workers in one ecosystem for better healthcare management.",
        "articles": [
            {
                "title": "How to Stay Healthy During Flu Season",
                "excerpt": "Tips on boosting your immunity and staying safe...",
                "link": "#"
            },
            {
                "title": "Kenya’s New Digital Health Policy",
                "excerpt": "The government is rolling out new initiatives for healthcare digitization...",
                "link": "#"
            },
            {
                "title": "Nutrition Matters: Eating Right Everyday",
                "excerpt": "A balanced diet is your best defense against chronic illness...",
                "link": "#"
            },
        ]
    }
    return render(request, "home.html", context)



@login_required
def dashboard_view(request):
    profile = request.user.profile

    if profile.role == "patient":
        history = MedicalHistory.objects.filter(patient=profile)
        # ✅ Fixed template path
        return render(request, "dashboards/patient_dashboard.html", {"profile": profile, "history": history})

    elif profile.role == "clinic_staff":
        # ✅ Fixed template path
        return render(request, "dashboards/clinic_staff_dashboard.html", {"profile": profile})

    elif profile.role == "doctor":
        # ✅ Fixed template path
        return render(request, "dashboards/doctor_dashboard.html", {"profile": profile})

    elif profile.role == "gov_official":
        # ✅ Fixed template path
        return render(request, "dashboards/gov_dashboard.html", {"profile": profile})

    elif profile.role == "chw":
        # ✅ Fixed template path
        return render(request, "dashboards/chw_dashboard.html", {"profile": profile})

    else:
        # ✅ Fixed template path
        return render(request, "dashboards/not_authorized.html")


@login_required
@role_required(['patient'])
def patient_dashboard(request):
    profile = request.user.profile
    # ✅ Added medical history like in dashboard_view
    history = MedicalHistory.objects.filter(patient=profile)
    return render(request, 'dashboards/patient_dashboard.html', {
        "profile": profile, 
        "history": history
    })

@login_required
@role_required(['clinic_staff'])
def clinic_staff_dashboard(request):
    profile = request.user.profile
    return render(request, 'dashboards/clinic_staff_dashboard.html', {"profile": profile})

@login_required
@role_required(['doctor'])
def doctor_dashboard(request):
    profile = request.user.profile
    return render(request, 'dashboards/doctor_dashboard.html', {"profile": profile})

@login_required
@role_required(['gov_official'])
def gov_dashboard(request):
    profile = request.user.profile
    return render(request, 'dashboards/gov_dashboard.html', {"profile": profile})

@login_required
@role_required(['chw'])
def chw_dashboard(request):
    profile = request.user.profile
    return render(request, 'dashboards/chw_dashboard.html', {"profile": profile})


def not_authorized_view(request):
    # ✅ Fixed template path
    return render(request, "dashboards/not_authorized.html")


@login_required
def redirect_to_dashboard(request):
    profile = request.user.profile

    if profile.role == "patient":
        return redirect('patient_dashboard')
    elif profile.role == "clinic_staff":
        return redirect('clinic_staff_dashboard')
    elif profile.role == "doctor":
        return redirect('doctor_dashboard')
    elif profile.role == "gov_official":
        return redirect('gov_dashboard')
    elif profile.role == "chw":
        return redirect('chw_dashboard')
    else:
        return redirect('not_authorized')