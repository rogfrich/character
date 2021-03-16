from django.contrib import admin
from .models import Character, CharacterClass, Race
# Register your models here.
admin.register(Character)
admin.register(CharacterClass)
admin.register(Race)