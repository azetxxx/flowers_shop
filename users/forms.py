from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Username',
        'type': 'text',
        'id': 'email',
        'name': 'name',
        'data-error': 'Please Enter Your Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password',
        'id': 'password',
        'name': 'name',
        'data-error': 'Please Enter Your Password',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'type': 'text',
        'id': 'first_name',
        'name': 'name',
        'data-error': 'Please Enter Your First Name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'type': 'text',
        'id': 'last_name',
        'name': 'name',
        'data-error': 'Please Enter Your Last Name',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'type': 'text',
        'id': 'username',
        'name': 'name',
        'data-error': 'Please Enter Your Username',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email-Address',
        'type': 'email',
        'id': 'email',
        'name': 'name',
        'data-error': 'Please Enter Your Email-Address',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password',
        'id': 'password1',
        'name': 'name',
        'data-error': 'Please Enter Your Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'type': 'password',
        'id': 'password2',
        'name': 'name',
        'data-error': 'This Password Should Match the Password Above',
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'readonly': True
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'readonly': True
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
