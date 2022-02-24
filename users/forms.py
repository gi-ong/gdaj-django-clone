from django import forms
from . import models
import re


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "ID", "id": "login_username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호", "id": "login_password"}
        )
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


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("username", "email")
        widgets = {
            "username": forms.TextInput(),
            "email": forms.EmailInput(),
        }

    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError(
                "That username is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        elif (
            len(password) < 8
            or len(password) > 21
            and not re.findall("[0-9]+", password)
            and not re.findall("[a-z]", password)
        ):
            raise forms.ValidationError(
                "Password 기준(8자리 이상 21자리 미만, 숫자,영문,대소문자 구성)에 맞지 않습니다."
            )
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user.username = username
        user.set_password(password)
        user.save()
