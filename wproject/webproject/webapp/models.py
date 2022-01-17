from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pic')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Peoples(models.Model):
    names=models.CharField(max_length=200)
    pic=models.ImageField(upload_to='pic')
    des=models.TextField()

    def __str__(self):
        return self.names