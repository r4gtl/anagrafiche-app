from django.db import models


class Cliente(models.Model):
    ragione_sociale = models.CharField(max_length=255)
    partita_iva = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)

class Fornitore(models.Model):
    ragione_sociale = models.CharField(max_length=255)
    partita_iva = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
