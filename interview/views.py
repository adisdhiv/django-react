from django.shortcuts import render, redirect
from .models import *
from .forms import ScheduleForm, InterviewerForm, CandidateForm


# Create your views here.
def home(request):
    schedule = Schedule.objects.all()
    totalcount = schedule.count()
    selected = schedule.filter(status = "Selected").count()
    context = {'totalcount' : totalcount, 'selected' : selected, 'schedule' : schedule}
    return render(request,'interview/home.html',context)

def candidates(request):
    candidates = Candidate.objects.all()
    context = {'candidates' : candidates}
    return render(request,'interview/candidates.html',context)

def interviewers(request):
    interviewers = Interviewer.objects.all()
    context = {'interviewers' : interviewers}
    return render(request,'interview/interviewers.html',context)

def createschedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request, 'interview/createschedule.html', context)

def updateschedule(request,pk):
    schedule = Schedule.objects.get(id = pk)
    form = ScheduleForm(instance=schedule)
    if request.method == 'POST':
        form = ScheduleForm(request.POST,instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request, 'interview/createschedule.html', context)

def deleteschedule(request,pk):
    schedule = Schedule.objects.get(id = pk) 
    if request.method == 'POST':
        schedule.delete()
        return redirect('/')
    context = {'item' : schedule}
    return render(request, 'interview/deleteschedule.html', context)

def createinterviewer(request):
    form = InterviewerForm()
    if request.method == 'POST':
        form = InterviewerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interviewers')
    
    context = {'form' : form}
    return render(request, 'interview/createinterviewer.html', context)

def updateinterviewer(request,pk):
    interviewer = Interviewer.objects.get(id = pk)
    form = InterviewerForm(instance=interviewer)
    if request.method == 'POST':
        form = InterviewerForm(request.POST,instance=interviewer)
        if form.is_valid():
            form.save()
            return redirect('interviewers')
    
    context = {'form' : form}
    return render(request, 'interview/createinterviewer.html', context)

def deleteinterviewer(request,pk):
    interviewer = Interviewer.objects.get(id = pk) 
    if request.method == 'POST':
        interviewer.delete()
        return redirect('interviewers')
    context = {'item' : interviewer}
    return render(request, 'interview/deleteinterviewer.html', context)

def createcandidate(request):
    form = CandidateForm()
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidates')
    
    context = {'form' : form}
    return render(request, 'interview/createcandidate.html', context)

def updatecandidate(request,pk):
    candidate = Candidate.objects.get(id = pk)
    form = CandidateForm(instance=candidate)
    if request.method == 'POST':
        form = CandidateForm(request.POST,instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidates')
    
    context = {'form' : form}
    return render(request, 'interview/createcandidate.html', context)

def deletecandidate(request,pk):
    candidate = Candidate.objects.get(id = pk) 
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidates')
    context = {'item' : candidate}
    return render(request, 'interview/deletecandidate.html', context)