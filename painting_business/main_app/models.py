from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class warehouse(models.Model):
    warehouse_id = models.CharField(max_length=20,verbose_name="Warehouse ID")
    warehouse_name = models.CharField(max_length=50,verbose_name="Warehouse Name")
    def __str__(self):
        return f"{self.warehouse_id}"

class painting_information(models.Model):
    painting_id = models.CharField(primary_key=True,max_length=30,verbose_name="Painting ID")
    artist_name = models.CharField(max_length=40,verbose_name="Artist Name")
    painting_name = models.CharField(max_length=60,verbose_name="Painting Name")
    price = models.IntegerField(default = None)
    available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to="media/",default=None)
    description = models.CharField(max_length=10000,default=None)
    def __str__(self):
        return f"{self.painting_id}"
    class Meta:
        verbose_name = "Painting Information"
        verbose_name_plural = "Painting Information"
        unique_together = ('painting_id','slug')

class tiers(models.Model):
    tier = models.IntegerField(primary_key=True,default=None)
    discount =  models.IntegerField(default=None)
    def __str__(self):
        return f"{self.tier}"
    class Meta:
        verbose_name = "Tier"
        verbose_name_plural = "Tiers"

class tiers_customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tier = models.ForeignKey(tiers,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}"

class order_information(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    painting = models.OneToOneField(painting_information,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}"
class warehouse_painting(models.Model):
    ware = models.OneToOneField(warehouse,on_delete=models.CASCADE,verbose_name="Warehouse ID")
    paint = models.OneToOneField(painting_information,on_delete=models.CASCADE,verbose_name="")
    def __str__(self):
        return f"{self.paint}"
    class Meta:
        verbose_name = "Warehouse Painting"
        verbose_name_plural = "Warehouse Paintings"











