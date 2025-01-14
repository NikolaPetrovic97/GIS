from django.db import models

class Mapa(models.Model):
    TopLlat = models.DecimalField(max_digits=11, decimal_places=8)
    TopLlon = models.DecimalField(max_digits=11, decimal_places=8)
    BotRlat = models.DecimalField(max_digits=11, decimal_places=8)
    BotRlon = models.DecimalField(max_digits=11, decimal_places=8)
    imgUrl = models.CharField(max_length=200)

    #def __str__(self):
        #return "String o mapi"
    
class Objekat(models.Model):
    TopLlat = models.DecimalField(max_digits=11, decimal_places=8)
    TopLlon = models.DecimalField(max_digits=11, decimal_places=8)
    BotRlat = models.DecimalField(max_digits=11, decimal_places=8)
    BotRlon = models.DecimalField(max_digits=11, decimal_places=8)
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE)

    #def as_json(self):
        #return dict(
            #id=self.id,
            #mapa_id=self.mapa.id,
            #BotRlon=str(self.BotRlon),
            #BotRlat=str(self.BotRlat),
            #TopLlon=self.TopLlon,
            #TopLlat=self.TopLlat)
