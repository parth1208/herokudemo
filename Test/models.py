from django.core.files import storage
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone=models.IntegerField(default=0)

class Category(models.Model):
    cat_type=(
        ('movies','movies'),
        ('webseries','webseries'),
        ('Anime','Anime')
    )
    category_type=models.CharField(choices=cat_type,max_length=25)
    category_name=models.CharField(max_length=25)
    category_desc=models.TextField()

    def __str__(self):
        return self.category_name

class Addmovies(models.Model):
    cat_types=(
        ('movies','movies'),
        ('webseries','webseries'),
        ('Anime','Anime')
    )
    movies_name=models.CharField(max_length=25)
    movies_image=models.ImageField(null=True,blank=True,upload_to='UserImage')
    category_types=models.CharField(choices=cat_types,max_length=25)
    movies_category=models.ForeignKey(Category,related_name='Category',on_delete=models.CASCADE)
    movies_discription=models.TextField()
    release_date=models.DateTimeField(auto_now_add=True)
    link=models.TextField()

    def __str__(self):
        s=str(self.movies_name)+' '+str(self.movies_category)
        return s