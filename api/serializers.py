from rest_framework import serializers
from .models import Action, Category, Product, Reference

from accounts.models import CustomUser

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        




class ActionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Action
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
    def validate_name(self, value):
        if value == 'admin':
            raise serializers.ValidationError('Name cannot be admin')
        return value  
    
    # def validate(self, attrs):
    #     if attrs['name'] == 'admin':
    #         raise serializers.ValidationError('Name cannot be admin')
    #     if attrs['description'] == 'admin':
    #         raise serializers.ValidationError('Description cannot be admin')
    #     return super().validate(attrs)  
        
        
    def create(self, validated_data):
        email = validated_data.pop('email')
        reference, created = Reference.objects.get_or_create(email=email)
        if not created:
            number = reference.number_of_references
            reference.number_of_references = number + 1
            reference.save()
        return super().create(validated_data)    
        
   
  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
        
class CategorySerialzerGetProduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        
class AuthorSerializerGetProduct(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']        


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    # author_full_name = serializers.CharField(source='author.get_full_name', read_only=True)
    # category_name = serializers.CharField(source='category.name', read_only=True)
    category_name = CategorySerialzerGetProduct(source='category', read_only=True)
    author_name = AuthorSerializerGetProduct(source='author', read_only=True)
    category_name_if_category_null = serializers.CharField(write_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'author', 'category_name', 'author_name']
    
    def validate(self, attrs):
        if attrs['category'] is None or attrs['category'] == '':
            category_name = attrs.pop('category_name_if_category_null')
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                category.description = 'This category was created automatically'
                category.save()    
            attrs['category'] = category
        return super().validate(attrs)    
        
    def create(self, validated_data):
        # get the user from the request
        user = self.context['request'].user # request.user
        validated_data['author'] = user
        return super().create(validated_data)  
    
    
    def validate_name(self, value):
        if value == 'admin':
            raise serializers.ValidationError('Name cannot be admin')
        return value 
        
     