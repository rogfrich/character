from django.db import models

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CharacterClass(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.name


class Character(models.Model):
    # Character info
    name = models.CharField(max_length=50, unique=True)
    level = models.IntegerField(default=1)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.PROTECT)

    # Abilities (NB ability mods are calculated in the view)
    ability_cha = models.IntegerField(default=8)
    ability_con = models.IntegerField(default=8)
    ability_dex = models.IntegerField(default=8)
    ability_int = models.IntegerField(default=8)
    ability_str = models.IntegerField(default=8)
    ability_wis = models.IntegerField(default=8)

    # Stats
    armour_class = models.IntegerField(default=5)
    initiative = models.IntegerField(default=2)
    proficiency = models.IntegerField(default=2)
    speed = models.IntegerField(default=30)


    def __str__(self):
        return self.name