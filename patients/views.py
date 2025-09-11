from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import MedicalHistory, UserProfile

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



def home_view(request):
    return render(request, 'home.html')




def patient_dashboard(request):
    # Get the logged-in user's profile
    profile = request.user.profile  

    # Make sure this user is a patient before showing patient dashboard
    if profile.role != "patient":
        # You can redirect staff/doctors to their own dashboards later
        return render(request, "not_authorized.html")

    # Fetch health data linked to this patient
    history = MedicalHistory.objects.filter(patient=profile)
    # prescriptions = Prescription.objects.filter(patient=profile)
    # labs = LabResult.objects.filter(patient=profile)

    return render(request, "dashboard.html", {
        "profile": profile,
        "history": history,
        # "prescriptions": prescriptions,
        # "labs": labs,
    })

