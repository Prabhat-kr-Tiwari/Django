from django.db import models

# Create your models here.
class MyModel(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.TextField()
    def __str__(self):
        return self.Name