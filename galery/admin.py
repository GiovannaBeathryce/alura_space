from django.contrib import admin
from galery.models import Photography

class ListPhotographys(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Photography, ListPhotographys)
