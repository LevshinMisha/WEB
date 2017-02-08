from django.contrib import admin
from .models import StudentsSkill, Student, Skill, Subject, Player, Stage, Choice


for i in [Subject, Skill, Student, StudentsSkill, Player, Stage, Choice]:
    admin.site.register(i)
