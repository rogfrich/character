from django.contrib import admin
from .models import \
    Character, \
    CharacterClass, \
    Race, \
    Weapon, \
    WeaponCategory, \
    Damage, \
    DamageType

# Register your models here.
admin.site.register(Character)
admin.site.register(Race)
admin.site.register(CharacterClass)
admin.site.register(Weapon)
admin.site.register(WeaponCategory)
admin.site.register(DamageType)
admin.site.register(Damage)