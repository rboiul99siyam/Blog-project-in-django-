from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,blank=True ,unique=True,null = True)
    def __str__(self) -> str:
        return self.name