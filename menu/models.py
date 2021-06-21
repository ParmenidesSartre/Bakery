from django.db import models
from django.db.models.fields import BooleanField
from django.urls import reverse
from django.utils.html import mark_safe
from django_resized import ResizedImageField
import math


class Menu(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,unique='name')
    after_discount = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    hot_item = models.BooleanField(default=False)
    added_on = models.DateField(auto_now_add=True)
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo =  ResizedImageField(size=[1000, 1077], crop=['middle', 'center'], upload_to='photos/%Y/%m/%d/',default='default.jpg')
    description = models.TextField(max_length=300, blank=True)
    best_seller = models.BooleanField()

    class Meta:
        ordering = ['-added_on']

    @property
    def thumbnail_preview(self):
        if self.photo:
            return mark_safe('<img src="{}" width="150" height="150" />'.format(self.photo.url))
        return ''    

    @property
    def discount(self):
      # discount value calculator
        if self.after_discount is not None:
            return str(math.floor((self.price - self.after_discount) / self.price * 100))
        else:
            return None

    def get_absolute_url(self):
        return reverse('cupcake', args=[self.slug])

    def __str__(self):
        return self.name
