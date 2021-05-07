from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserChangeForm, MyUserCreationForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    list_display = ("name", "surname", "email",)
    list_filter = ("is_admin","name", "surname", "email")

    fieldsets = (
        (None, {'fields': ('name', 'surname', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'surname', 'email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'name', 'surname')
    ordering = ('name',)
    filter_horizontal = ()


admin.site.register(MyUser, MyUserAdmin)
