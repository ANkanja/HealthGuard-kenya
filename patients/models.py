from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('clinic_staff', 'Clinic Staff'),
        ('doctor', 'Doctor'),
        ('gov_official', 'Government Official'),
        ('chw', 'Community Health Worker'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.user.username} ({self.role})"


# --- Signals: auto-create a profile when a User is created ---
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Only try saving if the related profile exists
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist:
        pass