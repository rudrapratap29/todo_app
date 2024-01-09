from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField()


class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete= models.CASCADE)
    title= models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
