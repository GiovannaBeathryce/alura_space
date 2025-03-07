from django.shortcuts import render, get_object_or_404
from galery.models import Photography

def index(request):

    photographys = Photography.objects.all()
    return render(request, 'galery/index.html', {'cards': photographys})
    
def image(request, photo_id):
    photography = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'galery/imagem.html', {'photography':photography})
