from django import forms
from django.forms import ModelForm

from .models import Student, Team, Donor

class StudentForm(ModelForm):
    student_name = forms.ModelChoiceField(queryset=Student.objects.all())
    student_phone = forms.TextInput()
    student_email = forms.TextInput()
    team = forms.ModelChoiceField(queryset=Team.objects.all())
    class Meta:
        model = Student
        fields= ['student_name', 'student_phone', 'student_email', 'team']


class DonorForm(ModelForm):
    donor_name = forms.TextInput()
    donor_phone = forms.TextInput()
    donor_email = forms.TextInput()
    donor_address = forms.TextInput()
    donor_student = forms.TextInput()
    class Meta:
        model = Donor
        # leaving out donor_student so the view fills in that input
        exclude = ('donor_student',)
        fields= ['donor_name', 'donor_phone', 'donor_email', 'donor_address']