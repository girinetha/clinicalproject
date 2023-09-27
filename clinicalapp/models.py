from django.db import models

# Create your models here.
class patient(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()

class clinicaldata(models.Model):
    COMPONENTNAMES={('hw','height/weight'),('bp','blood pressure'),('hr','heartrate')}
    componentname=models.CharField(choices=COMPONENTNAMES,max_length=20)
    componentvalue=models.CharField(max_length=20)
    measureddate=models.DateField(auto_now_add=True)
    patients=models.ForeignKey(patient,on_delete=models.CASCADE)