from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Address(models.Model):
    first_name = models.CharField(max_length=50,blank=True, verbose_name="prénom")
    last_name = models.CharField(max_length=50,blank=True, verbose_name="nom")
    house_number = models.IntegerField(verbose_name="numero")
    street = models.CharField(max_length=50, verbose_name="voie")
    postcode = models.PositiveSmallIntegerField(verbose_name="code postal")
    city = models.CharField(max_length=50, verbose_name="ville")
    phone = PhoneNumberField(region="FR", verbose_name="téléphone")
    infos = models.TextField(max_length=100, blank=True, verbose_name="informations supplémentaires")
    owner = models.ForeignKey(User, verbose_name=("propriétaire"),  on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('address:update', args=[self.pk])
    
    def __str__(self):
        return f'{self.house_number} {self.street} {self.postcode} {self.city}'
    
    def is_owned_by(self, user):
        return user == self.owner