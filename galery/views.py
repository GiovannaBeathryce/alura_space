from django.shortcuts import render, get_object_or_404
from galery.models import Photography

def index(request):

    photographys = Photography.objects.order_by('-id').filter(isPublic=True)
    return render(request, 'galery/index.html', {'cards': photographys})
    
def image(request, photo_id):
    photography = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'galery/imagem.html', {'photography':photography})

def search(request):
    photographys = Photography.objects.order_by('-id').filter(isPublic=True)
    
    if 'search' in request.GET:
        search_term = request.GET['search']
        if search_term:
            photographys = photographys.filter(name__icontains=search_term)

    return render(request, 'galery/search.html', {'cards': photographys})