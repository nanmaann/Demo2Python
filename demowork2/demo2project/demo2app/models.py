from django.db import models

# Create your models here.
class destinations(models.Model):
    heading=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    dis=models.TextField()

    def __str__(self):
        return self.heading

class profile(models.Model):
    name=models.CharField(max_length=150)
    pic=models.ImageField(upload_to='pics')
    disc=models.TextField()

    def __str__(self):
        return self.name
