from django.db import models

# Create your models here.



class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 30)
    email_adress = models.EmailField()
    adress = models.CharField(max_length = 150)
class Staff(User):
    status = models.CharField(max_length = 30)
class Student(User):
    id_student = models.CharField(max_length = 30)
class Proff(User):
    status = models.CharField(max_length = 30)
class Program(models.Model):
    name = models.CharField(max_length = 30) #LSD
    description = models.CharField(max_length = 200) 
class Level(models.Model):
    name_level = models.CharField(max_length = 200) #LSD3
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
class Module(models.Model):
    name = models.CharField(max_length = 30)
    level = models.ForeignKey(Level, on_delete = models.CASCADE)
class Course(models.Model):
    name = models.CharField(max_length = 30)
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    proffs = models.ManyToManyField(Proff)
 

class Form(models.Model):
    notes_cours = models.CharField(max_length = 200)
    notes_proff = models.CharField(max_length = 200)
    ameliorations = models.CharField(max_length = 200)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    module = models.ForeignKey(Module, on_delete = models.CASCADE)

class Question(models.Model):
    question_content = models.CharField(max_length = 200)
    choices = [('CM','Choix multiple'),
     ('CU','Choix unique'),
     ('TXT','Text')]
    question_type = models.CharField(choices = choices, max_length = 200)
    Forms = models.ManyToManyField(Form)