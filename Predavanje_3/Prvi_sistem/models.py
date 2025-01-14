from django.db import models

class Mapa(models.Model):
    TopLlat = models.DecimalField(max_digits=11, decimal_places=8)
    TopLlot = models.DecimalField(max_digits=11, decimal_places=8)
    BotRlat = models.DecimalField(max_digits=11, decimal_places=8)
    BotRat = models.DecimalField(max_digits=11, decimal_places=8)
    imgUrl = models.CharField(max_length=200)

    def __str__(self):
        return "String o mapi"

class Objekat(models.Model):
    TopLlat = models.DecimalField(max_digits=11, decimal_places=8)
    TopLlot = models.DecimalField(max_digits=11, decimal_places=8)
    BotRlat = models.DecimalField(max_digits=11, decimal_places=8)
    BotRat = models.DecimalField(max_digits=11, decimal_places=8)

    mapa=models.ForeignKey (Mapa, on_delete=models.CASCADE)
