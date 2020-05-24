from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
             'class' : "input-field",
             'label' : "Username",
            },
            ),
            required=True,
    )
    email = forms.EmailField( required = True),
    password = forms.CharField(widget=forms.PasswordInput(attrs={
             'class' : "input-field",
             'label' : "Password",
            },
            ),
            required=True,
            
    )
    class Meta():
        model = User
        fields = ('username','password','email')
