from django import forms
from .models import Stock, Portfolio

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['symbol', 'quantity', 'purchase_price']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
