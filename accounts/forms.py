from django import forms
from django.contrib.auth.models import User


class RegistroUserForm(forms.Form):
    """formulario de registro de usuarios"""
    username = forms.CharField(
        min_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        min_length=5,
        widget=forms.PasswordInput(attrs= {'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    photo = forms.ImageField(required=False)

    def clean_username(self):
        """Comprueba que no exista un esernameigual en la bd"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError("Nombre de usuario ya registrado")
        return username


    def clean_email(self):
        """Comprueba que no exista un email igual en la bd"""
        email = self.cleaned_data['email']
        if User.objects.filter(email = email):
            raise forms.ValidationError("ya existe un Email igual en la bd")
        return email

    def clean_password2(self):
        """Comprueba que los passwords sean identicos"""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2


class EditarEmailForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        """Obtener request"""
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        #comprobamos si ha cambiado el email
        actual_email = self.request.user.email
        username = self.request.user.username
        if email != actual_email:
            # si lo cambio, comprobar q no exista en la BD excluye el usuario actual
            existe = User.objects.filter(email=email).exclude(username=username)
            if existe:
                raise forms.ValidationError('Ya existe un email igual en la bd.')
        else:
            raise forms.ValidationError('No se detecto cambio de email.')
        return email


class EditarContrasenaForm(forms.Form):
    actual_password = forms.CharField(
        label='Contraseña actual',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        label='Nueva contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    password2 = forms.CharField(
        label='Repita su contraseña',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    def __init__(self, *args, **kwargs):
        """Obtener request"""
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)


    def clean_actual_password(self):
        password_actual = self.cleaned_data['actual_password']
        #password_actual = self.cleaned_data.get('password', None)
        if not self.request.user.check_password(password_actual):
            raise forms.ValidationError('Invalid password')

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2


class EditarImagenForm(forms.Form):
    photo = forms.ImageField(required=False)

