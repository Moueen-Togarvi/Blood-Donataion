from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'donor_id', 'is_suspended', 'is_donor')
    search_fields = ('donor_id', 'email', 'username', 'name')
    list_filter = ('is_suspended', 'is_donor', 'blood_group')

admin.site.register(User, UserAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
