from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import StudentInfo, Team, Donor, Roster

import re

class TeamForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())

class StudentSelect(forms.ModelForm):
    class Meta:
        model = StudentInfo
        exclude = ('team','pref_name', 'student_phone', 'student_email')
        fields = ('student_name',)
        labels = {
            'student_name': "Select your name"
        }
    def __init__(self, team, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_name'].queryset = Roster.objects.filter(team_id=team)

class StudentInfoForm(forms.ModelForm):
    # student_name = forms.ModelChoiceField(queryset=Roster.objects.all(), to_field_name='student_name')
    class Meta:
        model = StudentInfo
        exclude = ('team', 'student_name',)
        fields= ('pref_name', 'student_phone', 'student_email')
        labels = {
            'pref_name': "Your preferred name",
            'student_phone': "Phone number",
            'student_email': "Email address"
        }
    # def __init__(self, team, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['student_name'].queryset = Roster.objects.filter(team__roster=team)


STATE_CHOICES = [
    ('AL', 'Alabama'),('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),('CO', 'Colorado'),
    ('CT', 'Connecticut'),('DE', 'Delaware'),('DC', 'Washington D.C.') ,('FL', 'Florida'),('GA', 'Georgia'),
    ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
    ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'),
    ('MN', 'Minnesota'),('MS', 'Mississippi'),('MO', 'Missouri'),('MT', 'Montana') ,('NE', 'Nebraska'),('NV', 'Nevada'),
    ('NH', 'New Hampshire'),('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
    ('ND', 'Nort Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
    ('UT', 'Utah'), ('VT', 'Virginia'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming')
]

class DonorForm(ModelForm):
    donor_state = forms.CharField(widget=forms.Select(choices=STATE_CHOICES))
    class Meta:
        model = Donor
        # leaving out donor_student so the view fills in that input
        exclude = ('donor_student',)
        fields= ['donor_name', 'donor_phone', 'donor_email', 'donor_address', 'donor_city', 'donor_zip', 'donor_state']
        labels= dict(donor_state="State", donor_name="First and Last Name", donor_phone="Phone", donor_email="Email",
                     donor_address="Address", donor_city="City", donor_zip="Zipcode", )

    def __init__(self, *args, **kwargs):
        self.student = kwargs.pop('student', None)  # extract student from kwargs
        super().__init__(*args, **kwargs)

    def clean_donor_address(self):
        address = self.cleaned_data.get('donor_address', '')

        # Convert the entire address to title case
        address = address.title()

        # Convert directional words to their abbreviations
        address = address.replace('West', 'W').replace('East', 'E').replace('North', 'N').replace('South', 'S')

        # Replace all occurrences of "Th", "St", "Nd", etc., following a number with lowercase
        address = re.sub(r'(\d+)(St|Nd|Rd|Th)', lambda m: m.group(1) + m.group(2).lower(), address)

        # Define the mapping of full names to abbreviations
        abbreviations = {
            'Street': 'St',
            'Avenue': 'Ave',
            'Drive': 'Dr',
            'Circle': 'Cir',
            'Road': 'Rd',
            'Court': 'Ct',
            'Parkway': 'Pkwy',
            'Boulevard': 'Blvd',
            'Highway': 'Hwy',
            'Lane': 'Ln'
            # Add more mappings as needed
        }

        # Replace the full names with abbreviations
        for full, abbrev in abbreviations.items():
            address = re.sub(r'\b' + full + r'\b', abbrev, address)

        # Remove any periods following the abbreviations
        address = re.sub(r'(\bSt|\bAve|\bDr|\bCir)\.', r'\1', address)

        return address

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['donor_address'] = self.clean_donor_address()
        address = cleaned_data.get('donor_address')
        cleaned_data['donor_city'] = cleaned_data['donor_city'].title()
        cleaned_data['donor_name'] = cleaned_data['donor_name'].title()
        student = self.student
        if address and student and Donor.objects.filter(donor_address=address, donor_student=student).exists():
            raise ValidationError('You have already submitted a contact with that address.')
        return cleaned_data

class CoachForm(forms.Form):
    team = forms.ModelChoiceField(queryset = Team.objects.all())
    coach = forms.TextInput()