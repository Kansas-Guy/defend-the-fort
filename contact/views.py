from django.shortcuts import redirect, render
from .forms import StudentForm, DonorForm, TeamForm, CoachForm
from .models import StudentInfo, Team, Roster, Donor

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html')

def team(request):
    # anything that can be done to limit input error should be done
    if request.POST:
        form = TeamForm(request.POST)
        if form.is_valid():
            # grab team selection for form
            team_select = request.POST.get('team')

            # pass team_selection to student view
            return redirect('student', team_select)
    else:
        form = TeamForm()
    return render(request, 'contact/team.html', dict(form=TeamForm))

def student(request, team_select):

    if request.method == 'POST':
        form = StudentForm(team_select, request.POST)
        if form.is_valid():
            student_form = form.save(commit=False)
            # use team_select to fill out team field in form
            student_form.team = Team.objects.get(pk=team_select)
            student_form.save()
            student_name = request.POST.get('student_name')
            pref_name = request.POST.get('pref_name')
            form.save()
            # TODO fix the problem with multiple student_ids
                # should grab the pk from roster instead of studentinfo so there can only ever be one
            student_id = Roster.objects.get(pk=student_name).pk
            # student_id = student_id.last()
            # student_id = student_id.pk
        # send user to the donor form after completing their data
            return redirect(donors, student_id)
    else:
        form = StudentForm(team_select)

    return render(request, 'contact/student.html', dict(form=form,team_select=team_select))

def donors(request, student_id):
    donor_count = Donor.objects.filter(donor_student=student_id).count()
    if request.POST:
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            donor_contact = form.save(commit=False)
            donor_contact.donor_student = Roster.objects.get(pk=student_id)
            donor_contact.save()
            if donor_count < 10:
                return redirect(donors, student_id)
            else:
                return redirect(contact)

    else:
        form = DonorForm()

    return render(request, 'contact/donor.html', dict(form=form,student_id=student_id, donor_count=donor_count))

def coach(request):
    if request.POST:
        form = CoachForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            team = Team.objects.get(team_text = team).pk
            return redirect(dashboard, team)

    else:
        form = CoachForm()
    return render(request, 'contact/coach.html', dict(form=form))

def dashboard(request, team): # add team parameter after deciding how coach should "login"
    team_name = Team.objects.get(pk=team)
    team_name = team_name.team_text
    students = Roster.objects.filter(team=team)
    donor_count = { s.student_name: Donor.objects.filter(donor_student=s.pk).count() for s in students }
    return render(request, 'contact/dashboard.html', dict(team_name=team_name, donor_count=donor_count))