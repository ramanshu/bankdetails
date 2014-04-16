from django.db import models
from places.models import Location
class Bank(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)	
    country = models.CharField(max_length=50)
    website = models.URLField()

class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_description = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    address = models.ForeignKey(Location)
    bank = models.ForeignKey(Bank)
    ifsc_code = models.CharField(max_length=100)
    micr_code = models.CharField(max_length=100)
    bsr_code = models.CharField(max_length=100)
