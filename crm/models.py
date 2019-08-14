from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

from enum import Enum

# Create your models here.

# Comments:
# related_name='customers' es la inversa para llamar a los objetos customers.users o user.customers
class Customer(models.Model):
    name = models.CharField(max_length=140, null=True)
    last_name = models.CharField(max_length=140, null=True)
    middle_name = models.CharField(max_length=140, null=True)
    email = models.EmailField(max_length=140, null=True)
    phone = models.CharField(max_length=20, null=True)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='customers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# tupla de estatus proceso para generar enum en base de datos
STATUS_CHOICES = (
    (0 , 'nuevo') ,
    (1 , 'inservible'),
    (2 , 'contacto'),
    (3 , 'no_contactado'),
    (4 , 'contactado'),
    (5 , 'no_califica'),
    (6 , 'potencial'),
    (7 , 'promesa'),
    (8 , 'ganado'),
    (9 , 'cerrado'),
)

class Process(models.Model):
    status = models.CharField(choices=STATUS_CHOICES, default=0, max_length=20)
    color = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(Customer, related_name='process', on_delete=models.CASCADE)


    def __str__(self):
        return self.status

class Comment(models.Model):
    description = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    process = models.ForeignKey(Process, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class Task(models.Model):
    description = models.TextField(null=True)
    contact_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    process = models.ForeignKey(Process, related_name='tasks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)