from django.urls import path
from apps.galery.views import index, image, search, new_image, update_image, delet_image

urlpatterns = [
    path('', index, name='home'),
    path('imagem/<int:photo_id>', image, name='image'),
    path('search', search, name='search'),
    path('new-image', new_image, name='new_image'),
    path('update-image/<int:photo_id>', update_image, name='update_image'),
    path('delet-image/<int:photo_id>', delet_image, name='delet_image')
]