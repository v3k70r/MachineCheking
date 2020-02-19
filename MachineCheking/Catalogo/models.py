from django.db import models

class Marca(models.Model):
    nombreMarca =  models.CharField(default = "S/A", max_length = 200)
    telefonoMarca = models.IntegerField()
    descripcionMarca = models.CharField(default = "", max_length = 300)

    def __str__(self):
        return self.nombreMarca

class Categoria(models.Model):
    nombreCategoria = models.CharField(default = "S/A", max_length = 200)
    descripcionCategoria = models.CharField(default = "", max_length = 300)

    def __str__(self):
        return self.nombreCategoria


class Modelo(models.Model):
    nombreModelo = models.CharField(default = "S/A", max_length = 200)
    descripcion = models.CharField(default = "", max_length = 300)
    marcaModelo = models.ForeignKey(Marca, default = 1, on_delete = models.CASCADE )
    categoriaModelo = models.ForeignKey(Categoria, default=1, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombreModelo
