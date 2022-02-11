from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ID"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호"})
    )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist"))
