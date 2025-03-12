from django.urls import path
from galery.views import index, image, search

urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:photo_id>', image, name='image'),
    path('search', search, name='search')
]