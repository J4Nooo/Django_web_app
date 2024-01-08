from django.db import models

# Create your models here.
class Artykul(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=False)
    year = models.PositiveSmallIntegerField(default=2023)

    def __str__(self):
        return self.title


class Autor(models.Model):
    title = models.CharField(max_length=64)

class DataStworzenia(models.Model):
    Date = models.PositiveSmallIntegerField(default=2023)
class Dlugosc(models.Model):
    title = models.CharField(max_length=64)
