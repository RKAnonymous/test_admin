from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["email"]


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, widget=forms.EmailInput())
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())


class ManagerForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "phone", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user
