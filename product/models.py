from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)
    # parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)

    def __str__(self): return self.name


@receiver(pre_save, sender=Category)
def product_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='product_to_category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self): return f'{self.name} -> {self.price}$'

