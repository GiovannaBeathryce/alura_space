from django import forms

class LoginForms(forms.Form):
    name_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome de Login',
            }
        )
    )
    password=forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha',
            }
        )
    )


class RegisterForms(forms.Form):
    name_register=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nome de Cadastro',
            }
        )
    )
    
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=150,
        widget=forms.EmailInput(
             attrs={
                'class':'form-control',
                'placeholder':'Ex.: email@email.com',
            }
        )
    )

    password=forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha',
            }
        )
    )    

    confirm_password=forms.CharField(
        label='Confirme sua Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite novamente sua senha',
            }
        )
    )    