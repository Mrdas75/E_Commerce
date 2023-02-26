from django.db import models
from base.models import BaseModel
from django.utils.text import slugify  # slugify = it is a method which generate automatic slug

# Create your models here.


class Category(BaseModel):
    category_name=models.CharField(max_length=55)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField(upload_to="categories")

    def save(self , *args,**kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.category_name


class ColorVariant(BaseModel):
    color_name=models.CharField(max_length=89)
    price=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name


class SizeVariant(BaseModel):
    size_name=models.CharField(max_length=78)
    price=models.IntegerField()

    def __str__(self):
        return self.size_name

class Product(BaseModel):
    product_name = models.CharField(max_length=464)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category =models.ForeignKey(Category, on_delete=models.CASCADE,related_name="product")
    price = models.IntegerField()
    product_description = models.TextField()
    color_variant = models.ManyToManyField(ColorVariant,blank=True)
    size_variant = models.ManyToManyField(SizeVariant,blank=True)


    def save(self , *args,**kwargs):
        self.slug=slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.product_name
 
    def get_updated_price(self,size):
        return self.price + SizeVariant.objects.get(size_name=size).price




class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image",default="NO records")
    image=models.ImageField(upload_to="product",default="No images")






   
