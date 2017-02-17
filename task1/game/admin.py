from django.contrib import admin
from .models import Player, Stage, Choice


for i in [Player, Stage, Choice]:
    admin.site.register(i)
