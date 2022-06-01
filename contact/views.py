from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm, DonorForm, TeamForm
from .models import Student, Team

# Create your views here.

def index(request):
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
    return render(request, 'contact/index.html', dict(form=TeamForm))

def student(request, team_select):
    # establish team_select variable in view
    team_select=team_select
    if request.POST:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student_form = form.save(commit=False)
            # use team_select to fill out team field in form
            student_form.team = Team.objects.get(pk=team_select)
            student_form.save()
            student_name = request.POST.get('student_name')
            form.save()
        # send user to the donor form after completing their data
        return redirect(donors, student_name)

    return render(request, 'contact/student.html', dict(form=StudentForm,team_select=team_select))

def donors(request, student_name):
    # grabbing student_name from previous form to see on page
    student_name = student_name
    # use student_name to pull the student id that just filled out the form
    name = Student.objects.get(student_name = student_name)
    # trying to update this to show how many donors a student has submitted
    # look at inline formsets to have all donor forms on one page
    if request.POST:
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            donor_contact = form.save(commit=False)
            donor_contact.donor_student = name
            donor_contact.save()
            return redirect(index)

    else:
        form = DonorForm()

    return render(request, 'contact/donor.html', dict(form=DonorForm, student_name=student_name))