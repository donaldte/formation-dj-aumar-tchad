from rest_framework import serializers
from .models import Action


class ActionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Action
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters long')
        return value  
    
    def create(self, validated_data):
        email = validated_data.pop('email')
        print(email) # envoi un email a cette adresse
        return super().create(validated_data)  
        
        