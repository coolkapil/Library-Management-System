from operator import mod
from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

