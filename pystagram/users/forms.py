from django import forms
from django.core.exceptions import ValidationError
from users.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder": "사용자명 (3자리 이상)"},
        )
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (4자리 이상)"},
        )
    )

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명 ({username})은 이미 사용중입니다.", code="invalid")
        return username

    def clean(self):
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]
        if password != password2:
            self.add_error("password2", "비밀번호와 비밀번화 확인값이 다릅니다.")

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        profile_image = self.cleaned_data['profile_image']
        short_description = self.cleaned_data['short_description']

        user = User.objects.create_user(
            username = username,
            password = password,
            profile_image = profile_image,
            short_description = short_description,
        )

        return user