from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Project, Members, Contacts

import re


class ProjectForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.all())


class StudentSelect(forms.ModelForm):
    student_name = forms.ChoiceField(choices=[])

    class Meta:
        model = Members
        fields = ('student_name',)
        labels = {
            'student_name': "Select your name"
        }

    def __init__(self, project, *args, **kwargs):
        super().__init__(*args, **kwargs)
        student_choices = Members.objects.filter(project_id=project).order_by('student_name').values_list('id',
                                                                                                    'student_name')
        self.fields['student_name'].choices = student_choices


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        # leaving out donor_student so the view fills in that input
        exclude = ('contact_student',)
        fields = ['contact_first', 'contact_last', 'contact_phone', 'contact_email']
        labels = dict(contact_state="State", contact_first="First Name", contact_last="Last Name",
                      contact_phone="Phone",
                      contact_email="Email")

    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop('student', None)  # extract student from kwargs
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['contact_first'] = cleaned_data['contact_first'].title()
        cleaned_data['contact_last'] = cleaned_data['contact_last'].title()
        student = self.student
        return cleaned_data


class CoachForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Project.objects.all())
    coach = forms.TextInput()
