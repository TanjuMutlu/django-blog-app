from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanici Adi")
    password = forms.CharField(label="Parola",widget=PasswordInput)


class registerForm(forms.Form):
    username = forms.CharField(max_length=20,label="Kullanici Adi")
    password = forms.CharField(max_length=30,label="Parola",widget=PasswordInput)
    confirm = forms.CharField(max_length=30,label="Parolayi Dogrula",widget=PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eslesmiyor")
        
        values = {
            "username":username,
            "password":password
        }
        return values