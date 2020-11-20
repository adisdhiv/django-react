from django.forms import ModelForm
from .models import Schedule, Interviewer, Candidate

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

class InterviewerForm(ModelForm):
    class Meta:
        model = Interviewer
        fields = '__all__'

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'