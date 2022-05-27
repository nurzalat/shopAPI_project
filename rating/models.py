from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Mark:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    marks = (
        (one, 'Very Bad'),
        (two, 'Bad'),
        (three, 'Normal'),
        (four, 'Good'),
        (five, 'Super'),
    )


class Rating(models.Model):
    owner = models.ForeignKey(User, related_name='rating_to_user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='rating_to_product', on_delete=models.CASCADE)
    mark = models.PositiveSmallIntegerField(choices=Mark.marks)

    def __str__(self): return f'{self.mark} -> {self.product}'

    class Meta:
        unique_together = ('owner', 'product')
