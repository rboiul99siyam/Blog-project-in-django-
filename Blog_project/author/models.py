from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=50)
    phone_no = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name