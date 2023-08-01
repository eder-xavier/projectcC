from django.db import models

# Create your models here.
from django.db import models

class DadosGerais(models.Model):
    kic = models.IntegerField()
    Period = models.FloatField()
    Period_error = models.FloatField()
    bjd0 = models.FloatField()
    bjd0_error = models.FloatField()
    Period_td = models.FloatField()
    Period_errortd = models.FloatField()
    e = models.FloatField()
    e_error = models.FloatField()
    a = models.FloatField()
    a_error = models.FloatField()
    omega = models.FloatField()
    omega_error = models.FloatField()