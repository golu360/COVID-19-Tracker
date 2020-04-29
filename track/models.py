from django.db import models

# Create your models here.
class District(models.Model):
    district_name = models.CharField(max_length=100,blank=True)
    district_positive = models.IntegerField(null=False)
    district_tested = models.IntegerField(null=False)
    district_recovered = models.IntegerField(null=False)
    district_quarantined = models.IntegerField(null=False)
    district_deaths = models.IntegerField(null=False)
    updated_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.district_name



class Case(models.Model):
    description = models.CharField(max_length=1000,blank=True)
    coordinates_X = models.FloatField(max_length=100,blank=False,null=False)
    coordinates_Y = models.FloatField(max_length=100,blank=False,null=False)       