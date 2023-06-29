from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    Address = models.CharField(null=True, default=None, max_length = 200)
    ZipCode = models.CharField(default=0000, max_length = 9)
    
    

class Product(models.Model):
    NameProduct = models.CharField(max_length = 150)
    Description = models.CharField(max_length = 500)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Quantity = models.IntegerField(default=0)
    Img = models.URLField(max_length = 200)

    def __str__(self):
        return self.NameProduct
    
    
    
class Orders(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ordering user')
    ProdictID = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product Name')
    Number = models.IntegerField(verbose_name='ًQTY')
    TotalPrice = models.DecimalField(max_digits=5, decimal_places=2)
    TimeOrder = models.DateTimeField(auto_now=True, auto_now_add=False)

    s = (
        ('Waiting for confirmation', 'Waiting for confirmation'),
        ('Confirmed', 'Confirmed'),
        ('Sent', 'Sent'),
        ('Cancelled', 'Cancelled')
    )
    Status = models.CharField(choices=s,default=s[0][0],max_length=24)

    def __str__(self):
        return str(self.id)
    
    
    
    
    
    
    