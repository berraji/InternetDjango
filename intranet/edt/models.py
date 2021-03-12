from django.db import models

# Create your models here.

# EDT classes

class Class_(models.Model):

    name = models.CharField(max_length=200, null=True)

​

class Course(models.Model):

    name = models.CharField(max_length=200, null=True)

​

class Prof(models.Model):

    name = models.CharField(max_length=200, null=True)

    course = models.ForeignKey('Course', null=True, default=None, on_delete=models.CASCADE)

​

class Session(models.Model):

    start = models.TimeField(max_length=10)

    end = models.TimeField(max_length=10)

    types = [('P', 'Présentiel'), ('R', 'À distance')]

    type_ = models.CharField(choices=types, max_length=1, default=None)

    day = models.ForeignKey('Day', null=True, default=None, on_delete=models.CASCADE)

​

class Week(models.Model):

    start = models.DateField(max_length=10)

    end = models.DateField(max_length=10)

    hiliday = models.BooleanField(default=False)

    class_ = models.ForeignKey('Class_', null=True, default=None, on_delete=models.CASCADE)

​

class Day(models.Model):

    name = models.CharField(max_length=200, null=True)

    hiliday = models.BooleanField(default=False)

    date = models.DateField(max_length=10)

    week = models.ForeignKey('Week', null=True, default=None, on_delete=models.CASCADE)

​

class Request(models.Model):

    message = models.TextField(null=True)

    is_accepted = models.BooleanField(default=False)

    session = models.ForeignKey('Session', null=True, default=None, on_delete=models.CASCADE)

    prof = models.ForeignKey('Prof', null=True, default=None, on_delete=models.CASCADE)