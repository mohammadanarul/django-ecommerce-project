from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from .models import (
    Product,
    Brand,
    Category
)

@receiver(post_save, sender=Product)
def product_save(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()

@receiver(post_save, sender=Category)
def category_save(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()

@receiver(post_save, sender=Brand)
def brand_save(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()