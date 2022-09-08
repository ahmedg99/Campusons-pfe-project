from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Annonce(models.Model):
    Title=models.CharField(max_length=30,blank=True)
    TypeLogement=models.CharField(max_length=50 )
    NombreChambre=models.IntegerField()
    Surface=models.IntegerField()
    Emplacement=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    photo = models.ImageField(upload_to='annonce/') 
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='annonce',on_delete=models.CASCADE)
    NumTel=PhoneNumberField(blank=True)
    is_approved = models.BooleanField(default=False)
    prix = models.IntegerField(default=100)

  










