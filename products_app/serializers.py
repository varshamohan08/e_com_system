from django.shortcuts import get_object_or_404
from user_app.serializers import UserSerializer
from rest_framework import serializers
from .models import Category, Product
from django.conf import settings

from cryptography.fernet import Fernet

fernet = Fernet(settings.ENCRYPTION_KEY)

def encrypt_price(price) -> bytes:
    return fernet.encrypt(str(price).encode())

def decrypt_price(encrypted_price: bytes) -> str:
    try:
        decrypted_value = fernet.decrypt(encrypted_price).decode()
        return float(decrypted_value)
    except Exception as e:
        raise ValueError("Invalid encrypted price or key.")

class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M %p', read_only=True)
    updated_by = UserSerializer(read_only=True)
    updated_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M %p', read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_by', 'created_date', 'updated_by', 'updated_date']

    def validate(self, attrs):
        name = attrs.get('name')
        
        if self.instance:
            if Product.objects.filter(name=name).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError({'name': 'Product with this name already exists.'})
        else:
            if Product.objects.filter(name=name).exists():
                raise serializers.ValidationError({'name': 'Product with this name already exists.'})

        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['created_by'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        validated_data['updated_by'] = request.user
        return super().update(instance, validated_data)

class ProductSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M %p', read_only=True)
    updated_by = UserSerializer(read_only=True)
    updated_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M %p', read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 
                  'created_by', 'created_date', 'updated_by', 'updated_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['price'] = decrypt_price(instance.price)
        return representation

    def validate(self, attrs):
        name = attrs.get('name')
        
        if self.instance:
            if Product.objects.filter(name=name).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError({'name': 'Product with this name already exists.'})
        else:
            if Product.objects.filter(name=name).exists():
                raise serializers.ValidationError({'name': 'Product with this name already exists.'})

        return attrs

    def create(self, validated_data):
        # import pdb;pdb.set_trace()
        request = self.context.get('request')
        validated_data['price'] = encrypt_price(request.data.get('price', None))
        validated_data['created_by'] = request.user
        category_id = request.data.get('category', None)
        if category_id:
            validated_data['category'] = get_object_or_404(Category, id=category_id)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # import pdb;pdb.set_trace()
        request = self.context.get('request')
        validated_data['updated_by'] = request.user
        category_id = request.data.get('category', None)
        if category_id:
            validated_data['category'] = get_object_or_404(Category, id=category_id)
        price = request.data.get('price', None)
        if price:
            validated_data['price'] = encrypt_price(request.data.get('price', None))
        return super().update(instance, validated_data)
