from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    search_fields = ('phone', 'username', 'last_name')
    list_display = ('phone', 'id', 'username', 'last_name')


admin.site.register(User, UserAdmin)