from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class Account(User):
    PhoneNumber=PhoneNumberField(blank=True)
    Profilephoto = models.ImageField(upload_to='account/',blank=True)


class Question(models.Model):
    Question=models.CharField(max_length=80)
    Reponse=models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='question',on_delete=models.CASCADE)
    is_responded= models.BooleanField(default=False)