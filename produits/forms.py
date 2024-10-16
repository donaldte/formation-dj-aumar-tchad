from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=13)
    description = forms.Textarea(null=True, blank=True)
    price = forms.DecimalField(max_digits=100, decimal_places=2)
    

class ProductForm2(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        exclude = []
    