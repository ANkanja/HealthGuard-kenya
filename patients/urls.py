from django.urls import path
from .views import patient_dashboard, clinic_staff_dashboard, doctor_dashboard, gov_dashboard, chw_dashboard, register_view, UserLoginView, UserLogoutView, home_view, not_authorized_view, redirect_to_dashboard

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    # Dashboards
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('clinic_staff_dashboard/', clinic_staff_dashboard, name='clinic_staff_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('gov_dashboard/', gov_dashboard, name='gov_dashboard'),
    path('chw_dashboard/', chw_dashboard, name='chw_dashboard'),

     # Unauthorized
    path('not_authorized/', not_authorized_view, name='not_authorized'),

    # Dashboard redirect
    path('dashboard/', redirect_to_dashboard, name='redirect_to_dashboard'),
]