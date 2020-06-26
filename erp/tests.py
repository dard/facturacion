import os
from django.test import TestCase
from  erp import Type
from django.db.models import query
# Create your tests here.

#Listar
query  = Type.objects.all()

print(query)

#Insertar
t = Type()
t.name('Accionista')
t.save()

#edicion 
t = Type.objects.get(id=1)
print(t)

#eliminar
t = Type.objects.get(id=1)
t.delete()