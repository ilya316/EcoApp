from django.db import models

class Company(models.Model):
    name = models.CharField(verbose_name="Company name", max_length=100)
    description = models.TextField(verbose_name="Description")
    link = models.URLField(verbose_name="Link")
    logo = models.ImageField(verbose_name="Image")
    waste_types = models.ManyToManyField("Wastes.WasteTypes", verbose_name="Types of wastes")
    rate = models.IntegerField(verbose_name="Rate")

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    score = models.IntegerField(verbose_name="Score")
    text = models.TextField(verbose_name="Text")
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:15]