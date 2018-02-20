from django import forms


class Login (forms.Form):
    username = forms.CharField(max_length=150, label='Ник')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль', min_length=8)