from django.db import models as m

# Create your models here.

class employee(m.Model):
    MODE_CHOICES =[('female','female'),('male','male')]
    name=m.CharField(max_length=30)
    empid=m.IntegerField()
    age=m.IntegerField()
    place=m.CharField(max_length=30)
    gender=m.CharField(max_length=10,choices=MODE_CHOICES)
    joining_date=m.DateField()
    salary=m.IntegerField()
    designation=m.CharField(max_length=50)
    image=m.ImageField(upload_to="employee",null=True,blank=True)
