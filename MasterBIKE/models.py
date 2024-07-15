from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ELEGIR_REGION = (
('Arica y Parinacota', 'Arica y Parinacota'),
('Tarapacá', 'Tarapacá'),
('Antofagasta', 'Antofagasta'),
('Atacama', 'Atacama'),
('Coquimbo', 'Coquimbo'),
('Valparaíso', 'Valparaíso'),
('Metropolitana de Santiago', 'Metropolitana de Santiago'),
('Libertador General Bernardo O’Higgins', 'Libertador General Bernardo O’Higgins'),
('Maule', 'Maule'),
('Ñuble', 'Ñuble'),
('Biobío', 'Biobío'),
('La Araucanía', 'La Araucanía'),
('Los Ríos', 'Los Ríos'),
('Los Lagos', 'Los Lagos'),
('Aysén del General Carlos Ibáñez del Campo', 'Aysén del General Carlos Ibáñez del Campo'),
('Magallanes y la Antártica Chilena', 'Magallanes y la Antártica Chilena'),
)

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    price = models.FloatField()
    product_image = models.ImageField(upload_to='imgProductos')
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=70)
    telefono = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    region = models.CharField(choices=ELEGIR_REGION, max_length=100)
    def __str__(self):
        return self.nombre
    
class Carro(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    @property
    def total_costo(self):
        return self.cantidad * self.product.price
    



