from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    off_price=models.CharField(max_length=100,default=False)
class tip(models.Model):
    day=models.PositiveSmallIntegerField()
    month=models.TextField()
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()