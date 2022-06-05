from django import forms
from django.forms import ModelForm

from .models import StudentInfo, Team, Donor

class TeamForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())

class StudentForm(ModelForm):
    # student_name = forms.ModelChoiceField(queryset=StudentInfo.objects.all())
    # pref_name = forms.TextInput()
    # student_phone = forms.TextInput()
    # student_email = forms.TextInput()
    class Meta:
        model = StudentInfo
        exclude = ('team',)
        fields= ['student_name', 'pref_name', 'student_phone', 'student_email']
        labels = {
            'pref_name': "Your preferred name",
            'student_phone': "Phone number",
            'student_email': "Email address"
        }
    def __int__(self, team_id, *args, **kwargs):
        super(StudentForm, self).__int__(*args, **kwargs)
        self.fields['student_name'].queryset = StudentInfo.objects.filter(team=team_id)

STATE_CHOICES = [
     ('AL', 'Alabama'),('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),('CO', 'Colorado'),
    ('CT', 'Connecticut'),('DE', 'Delaware'),('DC', 'Washington D.C.'),('FL', 'Florida'),('GA', 'Georgia'),
    ('HI', 'Hawaii'),('ID', 'Idaho'),('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),('KS', 'Kansas'),
    ('KY', 'Kentucky'),('LA', 'Louisiana'),('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),('MI', 'Michigan'),
    ('MN', 'Minnesota'),('MS', 'Mississippi'),('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),('NV', 'Nevada'),
    ('NH', 'New Hampshire'),('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
    ('ND', 'Nort Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
    ('UT', 'Utah'), ('VT', 'Virginia'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming')
]

class DonorForm(ModelForm):
    donor_name = forms.TextInput()
    donor_phone = forms.TextInput()
    donor_email = forms.TextInput()
    donor_address = forms.TextInput()
    donor_city = forms.TextInput()
    donor_state = forms.CharField(widget=forms.Select(choices=STATE_CHOICES))
    donor_student = forms.TextInput()
    class Meta:
        model = Donor
        # leaving out donor_student so the view fills in that input
        exclude = ('donor_student',)
        fields= ['donor_name', 'donor_phone', 'donor_email', 'donor_address', 'donor_city', 'donor_state']