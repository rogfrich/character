from django.contrib import admin
from .models import Character, CharacterClass, Race
# Register your models here.
admin.site.register(Character)
admin.site.register(Race)
admin.site.register(CharacterClass)
