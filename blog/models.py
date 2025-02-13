from django.db import models
from account.models  import Karbar
# Create your models here
class  Post(models.Model):
    author = models.ForeignKey(Karbar ,on_delete=models.CASCADE)
    image= models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status =models.BooleanField()
    category= models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    Created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateField(auto_now=True)
    published_date=models.DateTimeField()

    def __str_(self):
        return  self.title
class Category(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return  self.name