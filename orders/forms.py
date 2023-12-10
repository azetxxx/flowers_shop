from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Max', 'required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Mustermann', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Your Email', 'required': False}))
    address1 = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Platz der Republik 1', 'required': False}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': '', 'required': False}))
    country = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'wide w-100', 'placeholder': 'Germany', 'required': False}))
    city = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'wide w-100', 'placeholder': 'Berlin', 'required': False}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': '11011', 'required': False}))

    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'email',
            'address1',
            'address2',
            'country',
            'city',
            'zip_code'
            )
