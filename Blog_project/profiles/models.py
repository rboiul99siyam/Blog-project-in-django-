from django.db import models

# Create your models here.
from author.models import Author

class Profile(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    author = models.OneToOneField(Author,models.CASCADE,default=None)
    def __str__(self) -> str:
        return self.name