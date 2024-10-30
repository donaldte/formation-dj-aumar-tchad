from django import forms
from .models import Product, Blog

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=13)
#     description = forms.Textarea(null=True, blank=True)
#     price = forms.DecimalField(max_digits=100, decimal_places=2)
    

# class ProductForm2(forms.ModelForm):
    
#     class Meta:
#         model = Product
#         fields = '__all__'
#         exclude = []
        
        
class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
        exclude = ['created_at', 'updated_at', 'user']
        
    def title_clean(self):
        title = self.cleaned_data.get('title')
        if title == 'title':
            raise forms.ValidationError('Title cannot be title')
        
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters')
        
        if Blog.objects.filter(title=title).exists():
            raise forms.ValidationError('Title already exists')
        
        return title          
    
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        
        if title == content:
            raise forms.ValidationError('Title and content must be different')
        

        return cleaned_data