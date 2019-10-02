from django import forms
from learn_django.models import Product

class productform(forms.ModelForm):

    class Meta:
        model = Product
        fields =('name','price','description')