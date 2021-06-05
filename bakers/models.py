from django.db import models
from django_resized import ResizedImageField

class Baker(models.Model):
    job = [
        ('Founder' , 'Founder'),
        ('Master Chef', 'Master Chef'),
        ('Master Baker', 'Master Baker'),
        ('Junior Baker', 'Junior Baker')
    ]
    name = models.CharField(max_length=100)
    designation = models.CharField(choices=job, max_length = 50, default='JuniorBaker')
    description = models.TextField(max_length=200)
    email = models.EmailField()
    photo =  ResizedImageField(size=[500, 300], crop=['middle', 'center'], upload_to='photos/%Y/%m/%d/',default='default.jpg')

    def __str__(self):
        return '{} - {}'.format(self.name, self.designation)