
from django.db import models
from datetime import datetime
from .choices import price_choices1, category_choices1, College_choices1,type1
from Core.models import User
# Create your models here.
class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=category_choices1)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=100,choices=type1)
    College = models.CharField(max_length=100,choices=College_choices1)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title