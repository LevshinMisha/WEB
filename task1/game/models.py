from django.db import models
from task1.settings import AUTH_USER_MODEL


class Student(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    name = models.CharField(max_length=20)
    money = models.PositiveIntegerField(default=2000)
    partner = models.BooleanField(default=False)
    happiness = models.PositiveIntegerField(default=50)
    tiredness = models.PositiveIntegerField(default=50)
    skills = models.ManyToManyField('Skill', through='StudentsSkill', through_fields=('student', 'skill'))
    #perks = models.ManyToManyField(Perks)

    def teach_subject(self, subj_name):
        subj = Subject.objects.get(name=subj_name)
        for skill in subj.connected_skills:
            StudentsSkill.objects.get(student=self, skill=skill).upgrade(subj.complexity)

    def __str__(self):
        return self.name


#class Perks(models.Model):
    #pass


#class Parents(models.Model):
    #pass


#class Random(models.Model):
    #pass


#class Roommate(models.Model):
    #pass


#class SubjectType(models.Model):
    #name = models.CharField()


class Skill(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Student)


class StudentsSkill(models.Model):
    skill = models.ForeignKey(Skill)
    student = models.ForeignKey(Student)
    score = models.PositiveIntegerField()
    complexity = models.FloatField()

    def upgrade(self, coeff):
        self.score += int(self.complexity * coeff)


class Subject(models.Model):
    name = models.CharField(max_length=20)
    complexity = models.FloatField()
    connected_subject = models.ForeignKey('self', blank=True)
    connected_skills = models.ManyToManyField(Skill)
    #type = models.ForeignKey(SubjectType)

    def connect_with_subject(self, subj):
        self.connected_subject = subj
        subj.connected_subject = self

    def __str__(self):
        return '{}(complexity={}, connected_with={})'.format(self.name, self.complexity, self.connected_subject.name)


