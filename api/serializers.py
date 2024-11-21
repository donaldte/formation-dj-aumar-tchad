from rest_framework import serializers
from .models import Action, Category, Reference


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
        
    