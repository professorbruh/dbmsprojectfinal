from django.db import models

# Create your models here.
class customer_information(models.Model):
    customer_id = models.CharField(primary_key=True,max_length=30,verbose_name="Customer ID")
    customer_name = models.CharField(max_length=40,verbose_name="Customer Name")
    email_id = models.CharField(max_length=40,verbose_name="Email ID")
    address = models.CharField(max_length=150,verbose_name="Address")
    def __str__(self):
        return f"{self.customer_id}"
    class Meta:
        verbose_name = "Customer Information"
        verbose_name_plural = "Customer Information"

class painting_information(models.Model):
    painting_id = models.CharField(primary_key=True,max_length=30,verbose_name="Painting ID")
    artist_name = models.CharField(max_length=40,verbose_name="Artist Name")
    painting_name = models.CharField(max_length=60,verbose_name="Painting Name")
    price = models.IntegerField(default = None)
    available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to="media/",default=None)

    def __str__(self):
        return f"{self.painting_id}"
    class Meta:
        verbose_name = "Painting Information"
        verbose_name_plural = "Painting Information"
        unique_together = ('painting_id','slug')

class sales_information(models.Model):
    customer_id = models.ForeignKey(customer_information,on_delete=models.CASCADE)
    painting_id = models.ForeignKey(painting_information,on_delete=models.CASCADE)
    issue_date = models.DateField(default=None)
    return_date = models.DateField(default=None)
    def __str__(self):
        return f"{self.customer_id},f{self.painting_id}"
    class Meta:
        verbose_name = "Sales Information"
        verbose_name_plural = "Sales Information"



