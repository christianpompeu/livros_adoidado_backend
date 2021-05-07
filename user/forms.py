from django.contrib.auth import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    password1 = CharField(label="Senha",widget=PasswordInput)
    password2 = CharField(label="Confirmação da senha",widget=PasswordInput)

    class Meta:
        model = MyUser
        fields = (
            "name",
            "surname",
            "email",
        )

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")

            if password1 and password2 and password1 != password2:
                raise ValidationError("As senhas não batem")
            return password2
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

class MyUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = (
            "name",
            "surname",
            "email",
        )

        def clean_password(self):
            return self.initial["password"]