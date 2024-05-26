from django.db import models
import datetime
# Create your models here.
class modelForm(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.AutoField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default="Rahim")
    boolean_field = models.BooleanField(default="True")
    date_field = models.DateField(default="2024-05-24")
    date_time_field = models.DateTimeField(default="2024-05-24 15:30:00.123456")
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default="5.67")
    email_field = models.EmailField(default="exmple@gmail.com")
    float_field = models.FloatField(default="4.56")
    generic_ip_address_field = models.GenericIPAddressField(default="192.0.2.1")
    text_field = models.TextField(default="asdfdf fdsf")
    

    
    def __str__(self) -> str:
        return f'name: {self.name} | roll: {self.roll} | address: {self.address}'