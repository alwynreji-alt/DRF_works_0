from django.db import models as m

# Create your models here.

class movie(m.Model):
    MODE_CHOICES =[('malayalam','malayalam'),('tamil','tamil'),('hindi','hindi'),('english','english')]
    title=m.CharField(max_length=30)
    director=m.CharField(max_length=30)
    language=m.CharField(choices=MODE_CHOICES)
    rating=m.FloatField()
    year=m.IntegerField()
    runtime=m.IntegerField()
    image=m.ImageField(upload_to="movie",null=True,blank=True)


