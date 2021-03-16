from django.db import models

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True)


class CharacterClass(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    level = models.IntegerField(default=1)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.PROTECT)
