from django.shortcuts import render
from .models import Character, Weapon, Damage
from .calculations import calculate_ability_mod


# Create your views here.
def index(request):
    character = Character.objects.get(pk=1)
    context = {
        "character": character,
        "ability_mod_cha": calculate_ability_mod(character.ability_cha),
        "ability_mod_con": calculate_ability_mod(character.ability_con),
        "ability_mod_dex": calculate_ability_mod(character.ability_dex),
        "ability_mod_int": calculate_ability_mod(character.ability_int),
        "ability_mod_str": calculate_ability_mod(character.ability_str),
        "ability_mod_wis": calculate_ability_mod(character.ability_wis),
    }

    weapons = []
    for weapon in character.weapons.all():
        weapon_damage = Damage.objects.filter(weapon=weapon)
        weapons.append(
            {"weapon_object": weapon,
             "weapon_damage": weapon_damage,

             }
        )

    context['weapons'] = weapons


    return render(request, "character_sheet/index.html", context=context)


def about(request):
    return render(request, "character_sheet/about.html")
