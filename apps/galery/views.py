from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Photography
from apps.galery.forms import PhotographyForms
from django.contrib import messages
from django.db.models import Q

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
            photographys = photographys.filter(
                Q(name__icontains=search_term) | 
                Q(caption__icontains=search_term) | 
                Q(description__icontains=search_term) | 
                Q(category__icontains=search_term) 
            )

        if not photographys.exists():
            messages.info(request, 'Nenhuma fotografia encontrada com esse termo.')

    return render(request, 'galery/index.html', {'cards': photographys})

def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    form = PhotographyForms
    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem adicionada com sucesso!')
            return redirect('home')
        
    return render(request, 'galery/new_image.html', {'form':form})

def update_image(request, photo_id):
    photo = Photography.objects.get(id=photo_id)
    form = PhotographyForms(instance=photo)

    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem atualizada com sucesso!')
            return redirect('home')

    return render(request, 'galery/update_image.html', {'form':form, 'photo_id':photo_id})

def delet_image(request, photo_id):
    photo = Photography.objects.get(id=photo_id)
    photo.delete()
    messages.success(request, 'Imagem deletada com sucesso!')
    return redirect('home')

def filter(request, category):
    photos = Photography.objects.filter(category=category)

    return render(request, 'galery/index.html', {'cards': photos})