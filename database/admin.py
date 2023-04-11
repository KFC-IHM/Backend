from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Restaurant, OpenHoursWeek, Review, Comment

admin.site.register(Restaurant)
admin.site.register(OpenHoursWeek)
admin.site.register(Review)
admin.site.register(Comment)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = UserAdmin.list_display + ('is_moderator', 'is_restaurateur', 'is_consumer')
