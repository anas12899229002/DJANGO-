from django.db import models

class TRAINPARIS (models.Model):
    vaultId = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 10)
    submap = models.CharField(max_length = 200)
    destination = models.CharField(max_length = 30, default='To NICE')
    logo = models.CharField(max_length = 50, default='To TOULOUS')
    time = models.IntegerField()