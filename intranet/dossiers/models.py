from django.db import models

# Create your models here.

class Level(models.Model):

    name = models.CharField(max_length=50)

    nb_of_years = models.IntegerField()

    Type = (

        ('L', 'Licence'),

        ('M', 'Master'),

        ('PHD', 'PHD'),

    )

class Student(models.Model):

	id_level = models.ForeignKey(

        'Level',

        on_delete=models.CASCADE,

    )

class Staff(models.Model):

    Type = (

        ('A', 'Administration'),

        ('F', 'Finance'),

    )

class File(models.Model):

    description = models.CharField(max_length= 300)

    nb_copies = models.IntegerField()

class Provided_Files(models.Model):

    path = models.CharField(max_length=300)

    physical_version = models.BooleanField(default= False)

class Dossier(models.Model):

    Type = (

        ('A', 'Administrative'),

        ('G', 'Scholarships'),

        ('F', 'Fees'),

    )

    description = models.CharField(max_length= 300)

class Containing(models.Model):

    id_dossier = models.ForeignKey(

        'Dossier',

        on_delete = models.CASCADE,

    )

    id_file = models.ForeignKey(

        'File',

        on_delete=models.CASCADE,

    )

class Specifying(models.Model):

    id_level = models.ForeignKey(

        'Level',

        on_delete=models.CASCADE,

    )

    id_file = models.ForeignKey(

        'File',

        on_delete=models.CASCADE,

    )

class Scholarship_Rate(models.Model):

    excellency = models.IntegerField()

    life_grant = models.IntegerField()

    id_student = models.ForeignKey(

        'Student',

        on_delete=models.CASCADE,

    )

class Scholarship_Affirmation(models.Model):

    id_staff = models.ForeignKey(

        'Staff',

        on_delete=models.CASCADE,

    )

     id_rate = models.ForeignKey(

        'Scholarship_Rate',

        on_delete=models.CASCADE,

    )

class Fees(models.Model):

    total_fees = models.IntegerField()

    paid_fees = models.IntegerField()

    id_student = models.ForeignKey(

        'Student',

        on_delete=models.CASCADE,

    )

class Fees_Affirmation(models.Model):

    id_fees = models.ForeignKey(

        'Fees',

        on_delete=models.CASCADE,

    )

    id_staff = models.ForeignKey(

        'Staff',

        on_delete= models.CASCADE

    )