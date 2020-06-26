from django.db import models
from datetime import datetime

# Create your models here.

class Type (models.Model):
    name = models.CharField(max_length = 150, verbose_name = 'Nombre', unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = [id]

class Category(models.Model):
    
    name = models.CharField(max_length = 150, verbose_name = 'Nombre')

    def __str__(self):
            return self.name

class Employed(models.Model):
    type = models.ForeignKey(Type,on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length = 150, verbose_name = 'Nombre')
    last_name = models.CharField(max_length = 150,verbose_name='Apellido')
    dni = models.CharField(max_length = 10, unique = True, verbose_name = 'Dni')
    date_sorted = models.DateField(default= datetime.now, verbose_name= 'Fecha de registro')
    date_creation = models.DateTimeField(auto_now= True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00,max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    #gender = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to = 'avatar/% Y/% m/% d/', null=True, blank= True)
    c_vitae = models.ImageField(upload_to = 'c_vitae/% Y/% m/% d/', null=True, blank= True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = [id]


