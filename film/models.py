from django.db import models

jins = (("erkak",'erkak'),("ayol","ayol"))
class Aktyor(models.Model):
    ism = models.CharField(max_length=150)
    davlat = models.CharField(max_length=50, blank=True, null=True)
    jins = models.CharField(max_length=5, choices=jins, blank=True, null=True)
    tugilgan_sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=150)
    janr = models.CharField(max_length=20, blank=True, null=True)
    yil = models.PositiveIntegerField(blank=True, null=True)
    aktyorlar = models.ManyToManyField(Aktyor)

    def __str__(self):
        return self.nom

class Tarif(models.Model):
    nom = models.CharField(max_length=150)
    davomiylik = models.CharField(max_length=40)
    narx = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nom

