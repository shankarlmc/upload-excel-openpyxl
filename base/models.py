from django.db import models
# Create your models here.


class ImportedData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
