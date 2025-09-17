from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, MedicalHistory, Prescription, LabResult


# Inline Profile for User Admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend the default User Admin to include UserProfile
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Custom UserProfile Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone_number', 'location')
    list_editable = ('role',)  # allows changing role directly in list view
    list_filter = ('role', 'location')  # filters in the sidebar
    search_fields = ('user__username', 'user__email', 'phone_number', 'location')

# Unregister the default User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(MedicalHistory)
admin.site.register(Prescription)
admin.site.register(LabResult)

