from django.db import models

# Create your models here.

opciones_consultas=[
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()
    mensaje = models.TextField()
    
    suscripcion = models.BooleanField()

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos",null=True)
    
    def __str__(self):
        return self.nombre