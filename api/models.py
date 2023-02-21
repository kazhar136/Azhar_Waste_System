from django.db import models

# Create your models here.

class Waste(models.Model):
    type1=[
        ('SOLID ','solid waste'),
        ('LIQUID','liquid waste'),
        ('HAZARDOUS','hazardous waste'),
        ('ORGANIC','organic waste')

    ]
    location = models.CharField(max_length=50)
    waste_type = models.CharField(max_length=100, choices=type1)
    waste_weight = models.CharField(max_length=50)
    added_date = models.DateField(auto_now_add=False,auto_now=False, blank=True)
