from django.contrib import admin
from galery.models import Photography

class ListPhotographys(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption', 'isPublic')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('isPublic',)

admin.site.register(Photography, ListPhotographys)