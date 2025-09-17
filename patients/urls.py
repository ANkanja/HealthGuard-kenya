from django.urls import path
from .views import patient_dashboard, clinic_staff_dashboard, doctor_dashboard, gov_dashboard, chw_dashboard, register_view, UserLoginView, UserLogoutView, home_view, not_authorized_view, redirect_to_dashboard, search_patients, view_patient_history, add_medical_history

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

    # Medical data
    path('search_patients/', search_patients, name='search_patients'),
    path('patient/<int:patient_id>/history/', view_patient_history, name='view_patient_history'),
    path('patient/<int:patient_id>/add_history/', add_medical_history, name='add_medical_history'),

    # Unauthorized
    path('not_authorized/', not_authorized_view, name='not_authorized'),

    # Dashboard redirect
    path('dashboard/', redirect_to_dashboard, name='redirect_to_dashboard'),

    # Medical Records features
    path('search_patients/', search_patients, name='search_patients'),
    path('patient/<int:patient_id>/history/', view_patient_history, name='view_patient_history'),
    path('patient/<int:patient_id>/history/add/', add_medical_history, name='add_medical_history'),
]