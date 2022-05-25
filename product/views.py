from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from product import serializers
from product.models import Product, Category


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    # serializer_class = serializers.ProductSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] #first method of setting permission

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        else:
            return serializers.ProductSerializer

    def get_permissions(self): #second method of setting permission
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny(),]
        else:
            return [permissions.IsAuthenticated(),]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAdminUser]
