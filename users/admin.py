from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'phone',
                    'avatar', 'is_superuser', 'is_staff', 'is_active']

    search_fields = ['username', 'first_name', 'last_name', 'email',]