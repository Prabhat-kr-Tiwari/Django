from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # You should hash the password before saving it.

    class Meta:
        app_label = 'signupapp'
    def __str__(self):
        return self.name