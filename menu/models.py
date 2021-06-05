from django.db import models
from django.db.models.fields import BooleanField

class Menu(models.Model):
    name = models.CharField(max_length=50)
    after_discount = models.DecimalField(max_digits=5,decimal_places=2,null = True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    hot_item = models.BooleanField(default=False)
    added_on = models.DateField(auto_now_add=True)
    photo =  models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=300, blank=True)
    best_seller = models.BooleanField()


    def __str__(self):
        return self.name