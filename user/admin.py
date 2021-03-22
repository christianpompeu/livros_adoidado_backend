from django import contrib
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordField
from .models import MyUser

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação da senha",widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = (
            "email",
            # "password"
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

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordField()

    class Meta:
        model = MyUser
        fields = (
            "email",
            "password"
        )

        def clean_password(self):
            return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email")
    list_filter = ("is_admin")

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
