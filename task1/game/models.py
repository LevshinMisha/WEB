from django.db import models
from task1.settings import AUTH_USER_MODEL
import json
from django.db.models import Model

def to_json(obj):
    if isinstance(obj, JsonDumpable):
        return obj.json()
    if type(obj) in [str, int, float]:
        return obj
    if type(obj) in [list, set]:
        return [to_json(i) for i in obj]
    if isinstance(obj, dict):
        return {key: to_json(obj[key]) for key in obj}
    if obj is None:
        return 'null'
    raise Exception


class JsonDumpable:
    def json(self):
        raise NotImplementedError

    def dump_to_json(self):
        return json.dumps(self.json())


class Student(Model):
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


class Skill(Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Student)


class StudentsSkill(Model):
    skill = models.ForeignKey(Skill)
    student = models.ForeignKey(Student)
    score = models.PositiveIntegerField()
    complexity = models.FloatField()

    def upgrade(self, coeff):
        self.score += int(self.complexity * coeff)


class Subject(Model):
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


class Stage(Model, JsonDumpable):
    code_name = models.CharField(max_length=30, unique=True)
    text = models.TextField()
    img = models.URLField()
    choices = models.ManyToManyField('self', through='Choice', through_fields=('stage_from', 'stage_to'), symmetrical=False)

    def __str__(self):
        return str(self.code_name)

    def get_choices(self):
        return Choice.objects.filter(stage_from=self)

    def json(self):
        return {
            'codeName': str(self.code_name),
            'text': str(self.text),
            'img': str(self.img),
            'choices': [i.json() for i in self.get_choices()]
        }


class Choice(Model, JsonDumpable):
    stage_from = models.ForeignKey(Stage, related_name='stage_from')
    stage_to = models.ForeignKey(Stage, related_name='stage_to')
    text = models.TextField()
    title = models.CharField(max_length=30)

    def __str__(self):
        return 'from:{} to:{} text:{}'.format(self.stage_from, self.stage_to, self.text)

    def json(self):
        return {
            'stage_from': str(self.stage_from),
            'stage_to': str(self.stage_to),
            'text': str(self.text),
            'title': str(self.title)
        }


class Player(Model, JsonDumpable):
    user = models.ForeignKey(AUTH_USER_MODEL)
    cur_stage = models.ForeignKey(Stage)

    def json(self):
        return {
            'user': str(self.user),
            'cur_stage': self.cur_stage.json()
        }

    def set_stage(self, stage):
        self.cur_stage = stage
        self.save()

    def __str__(self):
        return str(self.user)
