from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image']


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'title', 'description', 'icon']


class FeatureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureImage
        fields = ['id', 'image']


class ContainerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerImage
        fields = ['id', 'image']


class ItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemProduct
        fields = ['id', 'image', 'title', 'descriptions']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id','name', 'position', 'image', 'text']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'date', 'image']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'image', 'title', 'price']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'image']


class FeatureIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureIcon
        fields = ['id', 'title', 'description', 'icon']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'position', 'description', 'image']


class PostBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBlog
        fields = ['id', 'title', 'author', 'date', 'image']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'email', 'phn']


class Product1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product1
        fields = ['id', 'name', 'price', 'image', 'quantity']