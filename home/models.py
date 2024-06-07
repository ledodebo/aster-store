import uuid
from django.db import models
import datetime
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from django.conf import settings

from django_resized import ResizedImageField

class catagory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return self.name

class product(models.Model):
    brands = (
        ('v',"versatsse"),
        ('d',"dior"),
    )
    gender = (
        ('m',"male"),
        ('f',"female"),
        ('u',"unisex"),
    )
    name=models.CharField(max_length=50)
    image= ResizedImageField(size=[ 4578, 5723],crop= ["middle", "center"],upload_to="uploads/product")
    discount=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE,default=0)
    brand = models.CharField(max_length=1,choices= brands)
    genders = models.CharField(max_length=1,choices= gender)
    descretion=models.CharField(max_length=250,default="",blank=True,null=True)
    ava=models.BooleanField(default=True)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    size=models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.name
    
    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            size = (4578,5723)
            img  = Image.open(self.image.path)
            img.thumbnail(size,Image.LANCZOS)
            img.save(self.image.path)

class ProductVariation(models.Model):
    product = models.ForeignKey(product, related_name='variations', on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.kind}"
        
class gust(models.Model):
    name = models.CharField(max_length=100)
    #usser = models.OneToOneField(User,on_delete=models.CASCADE)
    #phone=models.CharField(max_length=50)
    device = models.CharField(max_length=100)
    #catagofavry=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    #order = customer=models.ForeignKey(order,on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return self.device
class CartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    device = models.CharField(max_length=100)
    gu = models.ForeignKey(gust, on_delete=models.CASCADE,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    session = models.CharField(max_length=100)
   # cart_id = models.UUIDField(default=uuid.uuid4 ,editable=False,primary_key=True)
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    

class order(models.Model):
    zone = (
        ('c',"القاهرة"),
        ('g',"الجيزة"),
        ('a',"العصيد"),
        ('d',"الدلتا"),
        ('b',"الغردقة-البحر-الاحمر"),
        ('s',"شرم-الشيخ-جنوب سيناء"),
        ('n',"المدن-الجديدة"),
        ('m',"مدينة-بدر"),
        ('x',"اسكندرية"),
        ('xs',"اطراف-الاسكندرية"),
        ('q',"القناة"),
    )
    iteams = models.CharField(max_length=250) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    email =models.CharField(max_length=250) 
    name = models.CharField(max_length=250)
    zones = models.CharField(max_length=2,choices=zone)
    adress=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    date=models.DateField(default=datetime.datetime.today)
    device = models.CharField(max_length=100)

    def __str__(self) :
        return self.adress
    
class inc(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      phone=models.CharField(max_length=250)


