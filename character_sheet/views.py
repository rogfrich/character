from django.shortcuts import render
from .models import Character


# Create your views here.
def index(request):
    character = Character.objects.get(pk=1)
    context = {
        "character": character
    }
    return render(request, "character_sheet/index.html", context=context)
