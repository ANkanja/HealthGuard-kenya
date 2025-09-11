from django.urls import path
from .views import patient_dashboard, register_view, UserLoginView, UserLogoutView, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'), 
]
