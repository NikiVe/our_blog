from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . models import User


class MyAdmin(UserAdmin):
    model = User
    list_display = ('id', 'email','last_login', 'first_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('id',)


admin.site.register(User, MyAdmin)
