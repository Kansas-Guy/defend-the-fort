from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name


class Members(models.Model):
    student_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student_email = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name


class Contacts(models.Model):
    contact_first = models.CharField(max_length=100)
    contact_last = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_student = models.ForeignKey(Members, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_first
