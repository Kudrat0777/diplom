from django import forms
from apps.users import models as user_models


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=20)