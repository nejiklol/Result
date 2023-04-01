from django.contrib import admin
from menu.models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'url', 'named_url']


admin.site.register(MenuItem, MenuItemAdmin)
