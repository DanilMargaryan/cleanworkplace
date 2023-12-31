from django.contrib import admin

from club.models import *


class CamerasAdmin(admin.ModelAdmin):
    list_display = ('ip', 'location', 'club')
    search_fields = ('ip', 'location', 'club')


admin.site.register(Club)
admin.site.register(Camera, CamerasAdmin)
admin.site.register(Picture)
