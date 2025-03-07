from django.shortcuts import render

def index(request):

    dados = {
        1: {"nome":"Nebulosa de Carina",
            "legenda":"webbtelescope.org / NASA / James Webb"},
        2: {"nome":"Galáxia NGC 1079",
            "legenda":"nasa.org / NASA / Hubble"}
        }
    
    return render(request, 'galery/index.html', {'cards': dados})
    
def image(request):
    return render(request, 'galery/imagem.html')
