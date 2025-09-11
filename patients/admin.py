from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, MedicalHistory

# Register your models here.


# Define an inline admin for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# Extend the default User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Re-register User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "condition", "date_diagnosed")
    list_filter = ("date_diagnosed",)
    search_fields = ("condition", "notes", "patient__user__username")
