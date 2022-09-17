from django.contrib import admin
from .models import *


admin.site.register(Section)
admin.site.register(Theme)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'date',
    )
    ordering = ('date',)

@admin.register(SideMenuItem)
class SideMenuItemAdmin(admin.ModelAdmin):
    pass
