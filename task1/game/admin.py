from django.contrib import admin
from .models import StudentsSkill, Student, Skill, Subject


admin.site.register(Subject)
admin.site.register(Skill)
admin.site.register(Student)
admin.site.register(StudentsSkill)
