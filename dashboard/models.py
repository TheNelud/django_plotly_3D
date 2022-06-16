from django.db import models

# Create your models here.
class Dashboard(models.Model):
    skv_name = models.CharField(max_length=100)
    skv_x = models.FloatField()
    skv_y = models.FloatField()
    skv_z = models.FloatField()
    status = models.BooleanField(default=True)

