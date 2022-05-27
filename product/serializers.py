from rest_framework import serializers
from product.models import Category, Product
from django.db.models import Avg


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rating'] = instance.rating_to_product.aggregate(Avg('mark'))
        return representation


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rating'] = instance.rating_to_product.aggregate(Avg('mark'))
        return representation


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductListSerializer(instance.product_to_category.all(), many=True).data

        return representation
