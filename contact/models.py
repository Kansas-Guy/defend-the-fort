from django.db import models

# Create your models here.
class Team(models.Model):
    team_text = models.CharField(max_length=50)
    coach = models.CharField(max_length=100)
    def __str__(self):
        return self.team_text

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=20)
    student_email = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

class Donor(models.Model):
    donor_name = models.CharField(max_length=100)
    donor_email = models.CharField(max_length=100)
    donor_phone = models.CharField(max_length=20)
    donor_address = models.CharField(max_length=200)
    donor_student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.donor_name