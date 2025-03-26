from django import forms
from apps.galery.models import Photography

class PhotographyForms(forms.ModelForm):
    class Meta:
        model = Photography
        exclude = ['isPublic',]
        labels = {
            'name': 'Nome',
            'caption': 'Legenda',
            'category': 'Categoria',
            'description': 'Descrição',
            'photo': 'Imagem',
            'user': 'Usuário',
        }

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'caption':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
        }