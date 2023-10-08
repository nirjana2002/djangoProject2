from django.db import models

# Create your models here.
from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    CEO_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    number_of_branches = models.IntegerField()
    number_of_employees = models.IntegerField()

    def __str__(self):
        return 'Name: ' + self.name + '--> CEO Name: ' + self.CEO_name
