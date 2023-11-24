from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

upload_storage = FileSystemStorage(location=settings.STATIC_ROOT, base_url='/static')

class WasteTypes(models.Model):
    type = models.CharField(verbose_name="Type name", max_length=100, default="type")
    description = models.TextField(verbose_name="Description", default="description")
    yard_type = models.CharField(verbose_name="Yard type", max_length=100)
    icon = models.ImageField(verbose_name="Waste type icon", null=True, blank=True, upload_to="static/images/waste_type_icon/")

    def __str__(self):
        return self.type

class WasteSite(models.Model):
    name = models.CharField(verbose_name="Name",max_length=100)
    address = models.CharField(verbose_name="Addres", max_length=255)
    yard_type = models.CharField(verbose_name="Yard_type", max_length=100)
    lattitude = models.FloatField(verbose_name="Lattitude", default=0)
    longitude = models.FloatField(verbose_name="Longitude", default=0)

    def __str__(self):
        return self.name
    
class WasteExample(models.Model):
    name = models.CharField(verbose_name="Wast name", max_length=100)
    waste_type = models.ForeignKey(WasteTypes, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(verbose_name="Waste image", null=True, blank=True, upload_to="static/images/waste_example_photo/")
    description = models.TextField(verbose_name="Desc")

    def __str__(self):
        return self.name