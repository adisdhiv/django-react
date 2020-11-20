from django.test import TestCase
from interview.models import Candidate, Interviewer, Schedule
from django.utils import timezone

# Create your tests here.

class CandidateModelTest(TestCase):
    def test_candidatemodel(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        self.assertEqual(str(cand),cand.name)

class InterviewModelTest(TestCase):
    def test_interviewmodel(self):
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        self.assertEqual(str(inter),inter.name)

class ScheduleModelTest(TestCase):
    def test_schedulemodel(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        sch = Schedule.objects.create(candidate = cand, ipanel = inter)
        self.assertEqual(str(sch),sch.candidate.name)
