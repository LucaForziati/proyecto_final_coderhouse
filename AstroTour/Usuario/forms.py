from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Astroturista, Acompañantes

from django.contrib.auth import authenticate, get_user_model, password_validation

from django.core.exceptions import ValidationError

#############################################

class Astroturista_formulario(forms.ModelForm):

    class Meta:

        model = Astroturista
        fields = ('pasaporte_espacial','nombre', 'apellido', 'email', 'peso', 'avatar', )
        widgets = {
            'pasaporte_espacial':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'nombre':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'apellido':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su email',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'peso':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ubicacion del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
        }
        

class Acompañantes_formulario(forms.ModelForm):

    class Meta:

        model = Acompañantes
        fields = ('nombre', 'apellido', 'pasaporte_espacial','peso')

class UserEditForm(UserCreationForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = ['password1', 'password2'] 
        help_texts = {k:"" for k in fields}

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        widgets = {
            'username':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'email':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ubicacion del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'first_name':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese kilometros al destino (desde la tierra)',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'last_name':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese gravedad del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
        }
    


class AstroturistaEditForm(Astroturista_formulario):

    pasaporte_espacial = forms.IntegerField(label = "Modifica tu pasaporte espacial")
    nombre = forms.CharField(max_length = 30, label = "Modifica tu nombre")
    apellido = forms.CharField(max_length = 30, label = "Modifica tu apellido")
    email = forms.CharField(max_length = 30, label = "Modifica tu email")
    peso = forms.IntegerField(label = "Modifica tu peso")
    avatar = forms.ImageField( label = "Modifica tu avatar")


    class Meta:

        model = Astroturista
        fields = ('pasaporte_espacial','peso', 'avatar')
        help_texts = {k:"" for k in fields}


class SuperUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label= ("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text= ("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username","is_superuser", "is_staff")
        field_classes = {"username": UsernameField, "email": forms.EmailField, "first_name": forms.CharField, "last_name": forms.CharField, "is_superuser": forms.BooleanField, "is_staff": forms.BooleanField}
        widgets = {
            'username':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'email':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ubicacion del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'first_name':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese kilometros al destino (desde la tierra)',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'last_name':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese gravedad del destino',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'is_superuser': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'for': 'form-check-input',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
            'is_staff': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'for': 'form-check-input',
                    'cols': '1px',
                    'rows': '1px'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user