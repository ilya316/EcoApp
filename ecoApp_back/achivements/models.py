from django.db import models

class Achivement(models.Model):
    name = models.CharField(verbose_name="Achive name", max_length=100)
    description = models.TextField(verbose_name="Description")
    icon = models.ImageField(verbose_name="Image")
    value = models.IntegerField(verbose_name="Demanded amount")
    # value_type = models.

    def __str__(self):
        return self.name