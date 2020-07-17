from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Subcategory(models.Model):
    catid = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
