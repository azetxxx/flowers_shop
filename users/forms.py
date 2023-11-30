import uuid
from datetime import timedelta
from typing import Any

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from users.models import EmailVerification, User


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

    def is_activated(self):
        user = self.get_user()
        if user.is_verified_email:
            return True
        else:
            return False

    def clean(self):
        # First call the clean method of the parent class
        super().clean()

        # Now check if the user's email is verified
        if not self.is_activated():
            error_messages = {
                "invalid_login": _(
                    "Please verify your account for %(username)s during 48 hours after registration. "
                    "Check your email for the verification link."
                ),
                "inactive": _("This account is inactive."),
            }
            # Raise the specific error message
            raise ValidationError(
                error_messages["invalid_login"],
                code='invalid_login',
                params={'username': self.cleaned_data.get('username')}
            )

        # If everything is fine, return the cleaned data
        return self.cleaned_data


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

    def save(self, commit: bool = ...) -> Any:
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user


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
