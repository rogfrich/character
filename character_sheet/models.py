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


class WeaponCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Weapon category"
        verbose_name_plural = "Weapon categories"

    def __str__(self):
        return self.name


class DamageType(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Damage type"

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(WeaponCategory, on_delete=models.PROTECT)
    weight_lbs = models.DecimalField(max_digits=5, decimal_places=2)
    modifying_ability = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Damage(models.Model):
    damage_type = models.ForeignKey(DamageType, on_delete=models.PROTECT)
    weapon = models.ForeignKey(Weapon, on_delete=models.PROTECT)
    dice_type = models.IntegerField(default=6)
    dice_qty = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Damage"

    def __str__(self):
        return f"{self.weapon.name}: {self.damage_type.name.lower()}"


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

    # Weapons
    weapons = models.ManyToManyField(Weapon)

    def __str__(self):
        return self.name
