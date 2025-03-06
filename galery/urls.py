from django.urls import path
from galery.views import index, image

urlpatterns = [
    path('', index, name='home'),
    path('imagem/', image, name='image'),
]