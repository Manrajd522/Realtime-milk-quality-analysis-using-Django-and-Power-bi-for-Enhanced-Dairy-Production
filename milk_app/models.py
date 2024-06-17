from django.db import models
from datetime import date


# Create your models here.
class User(models.Model):
    User_id = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=100)
    Phone_No = models.CharField(max_length=15 ,null= True)  # Use CharField to accommodate various phone number formats
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.User_id


class Record(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE  )
    Date = models.DateField(default=date.today)
    Quantity = models.DecimalField(max_digits=6, decimal_places=2)
    Fat = models.DecimalField(max_digits=4, decimal_places=2)
    SNF = models.DecimalField(max_digits=4, decimal_places=2)
    Amount = models.DecimalField(max_digits = 10, decimal_places=4)



