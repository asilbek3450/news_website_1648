from django.db import models
# import django User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):

    def __str__(self):
        return self.username
    

class Category(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi
    

class News(models.Model):
    nomi = models.CharField(max_length=255)
    rasmi = models.ImageField(upload_to='news_images/')
    content = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)  # auto_now bilan farqini o'rganish

    def __str__(self):
        return self.nomi
    

class Comment(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)  # auto_now bilan farqini o'rganish

    def __str__(self):
        return f'{self.user_id} - {self.news_id}'


