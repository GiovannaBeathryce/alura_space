from django.contrib import admin
from apps.galery.models import Photography

class ListPhotographys(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption', 'isPublic')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category','user')
    list_editable = ('isPublic',)

admin.site.register(Photography, ListPhotographys)