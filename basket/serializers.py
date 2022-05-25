from rest_framework import serializers

from basket.models import Basket
from product.models import Product


class BasketSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            product = Product.objects.get(pk=attrs['product'])
        except Product.DoesNotExist:
            serializers.ValidationError('Product not found')
        quantity = attrs['quantity']
        data['product'] = product.pk
        # data['product'] = product
        data['quantity'] = quantity
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Product.objects.get(pk=data['product'])
        Basket.objects.create(user=user, product=product, quantity=data['quantity'],)
        # Basket.objects.create(user=user, product=data['product'], quantity=data['quantity'], )

