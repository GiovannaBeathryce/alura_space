from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Photography
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')

    photographys = Photography.objects.order_by('-id').filter(isPublic=True)
    return render(request, 'galery/index.html', {'cards': photographys})
    
def image(request, photo_id):
    photography = get_object_or_404(Photography, pk=photo_id)
    return render(request, 'galery/imagem.html', {'photography':photography})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')

    photographys = Photography.objects.order_by('-id').filter(isPublic=True)
    
    if 'search' in request.GET:
        search_term = request.GET['search']
        if search_term:
            photographys = photographys.filter(name__icontains=search_term)

    return render(request, 'galery/search.html', {'cards': photographys})