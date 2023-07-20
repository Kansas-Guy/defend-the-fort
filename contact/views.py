from django.shortcuts import redirect, render
from .forms import StudentInfoForm, DonorForm, TeamForm, CoachForm, StudentSelect
from .models import StudentInfo, Team, Roster, Donor
from rest_framework import viewsets
from .serializers import DonorSerializer, RosterSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

def student(request, team_select): # view for selecting student name

    if request.method == 'POST':
        form = StudentSelect(team_select, request.POST)
        if form.is_valid():
            student_name = request.POST.get('student_name')
            student_id = Roster.objects.get(pk=student_name).pk
            if StudentInfo.objects.filter(student_name_id=student_id).exists() != True:
                return redirect(student_info, student_id, team_select)
            # check to see if student has provided their info
            else:
                return redirect(donors, student_id)
    else:
        form = StudentSelect(team_select)

    return render(request, 'contact/student.html', dict(form=form,team_select=team_select))

def student_info(request, student_id, team_select):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            student_form = form.save(commit=False)
            # use team_select to fill out team field in form
            student_form.team = Team.objects.get(pk=team_select)
            # use student_id to fill out student_name field in form
            student_form.student_name = Roster.objects.get(pk=student_id)
            student_form.save()
            form.save()
        # send user to the donor form after completing their data
            return redirect(donors, student_id)
    else:
        form = StudentInfoForm()

    return render(request, 'contact/student-info.html', dict(form=form,team_select=team_select, student_id=student_id))

def donors(request, student_id):
    donor_count = Donor.objects.filter(donor_student=student_id).count()
    s_donors = Donor.objects.filter(donor_student_id=student_id)
    student = Roster.objects.get(pk=student_id)

    if request.method == 'POST':
        form = DonorForm(request.POST, student=student)

        if form.is_valid():
            donor_contact = form.save(commit=False)
            donor_contact.donor_student = student
            form.instance = donor_contact
            donor_contact.save()

            if donor_count < 10:
                return redirect(donors, student_id)
            else:
                return redirect(review, student_id)
        else:
            print(form.errors)

    else:
        form = DonorForm(student=student)

    return render(request, 'contact/donor.html', dict(form=form,student_id=student_id, donor_count=donor_count,
                                                      s_donors=s_donors))

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

def dashboard(request, team): # Donor information for each student needs to be passed
    team_name = Team.objects.get(pk=team)
    team_name = team_name.team_text
    students = Roster.objects.filter(team=team)
    student_info = []
    for s in students:
        studentDict = {
            'name': s.student_name,
            'donor_count': Donor.objects.filter(donor_student=s.pk).count(),
            'student_id': s.pk,
        }
        student_info.append(studentDict)


    return render(request, 'contact/dashboard.html', dict(team_name=team_name, student_info=student_info))

def donor_review(request, student_id):
    student = Roster.objects.get(pk=student_id)
    name = student.student_name
    donors = Donor.objects.filter(donor_student_id=student_id)
    return render(request, 'contact/donor_review.html', dict(donors=donors, name=name))


def review(request, student_id):
    s_donors = Donor.objects.filter(donor_student_id=student_id)
    return render(request, 'contact/review.html', dict(student_id=student_id, s_donors=s_donors))

def donor_edit(request, donor_id):
    donor = Donor.objects.get(id=donor_id)
    student_id = donor.donor_student_id

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect(donors, student_id)
    else:
        form = DonorForm(instance=donor)
    return render(request, 'contact/donor_edit.html', dict(donor_id=donor_id, form=form, student_id=student_id))

class DonorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class RosterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer

@api_view(['GET'])
def donors_for_student(request, student_id):
    student = get_object_or_404(Roster, pk=student_id)
    donors = Donor.objects.filter(donor_student=student)
    serializer = DonorSerializer(donors, many=True)
    return Response(serializer.data)