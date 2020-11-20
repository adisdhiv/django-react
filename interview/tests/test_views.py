from django.test import TestCase
from interview.forms import ScheduleForm, InterviewerForm, CandidateForm
from interview.models import Candidate, Interviewer, Schedule
from django.utils import timezone
from django.urls import reverse

class ViewsHomepageTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class ViewsCandidatesTest(TestCase):
    def test_candidatepage(self):
        response = self.client.get('/candidates/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/candidates.html")

class ViewsInterviewersTest(TestCase):
    def test_interviewerpage(self):
        response = self.client.get('/interviewers/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/interviewers.html")

#class ViewsCreatescheduleTest(TestCase):
    #def test_createschedulepage(self):
        #response = self.client.get('/createschedule')
        #self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, "interview/createschedule.html")
        #cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        #inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        #res = self.client.post('/createschedule', 
        #    {'candidate': cand,
        #     'ipanel': inter ,
        #     'position' : 'Developer',
        #     'status' : 'Selected',
        #     'interviewname' : 'IBM',
        #     'interviewtype' : 'Teams' ,
        #     'interviewtime' : timezone.now(),
        #     'interviewdate' : '2020-10-10',
        #     'remarks' : 'good'
        #})
        #self.assertRedirects(res, 'home')

class ViewsCreateCandidate(TestCase):
    def test_createcandidate(self):
        response = self.client.get('/createcandidate')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/createcandidate.html")
        res = self.client.post('/createcandidate', {
            'name': 'candiname',
            'phone': '1341',
            'email': "ef@g.com",
        })
        self.assertRedirects(res, '/candidates/')

class ViewsCreateInterviewer(TestCase):
    def test_createinterviewer(self):
        response = self.client.get('/createinterviewer')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/createinterviewer.html")
        res = self.client.post('/createinterviewer', {
            'name': 'interviewer',
            'phone': '1341',
            'email': "ef@g.com",
        })
        self.assertRedirects(res, '/interviewers/')

class ViewsupdateCandidate(TestCase):
    def test_updatecandidate(self):
        response = self.client.get('/createcandidate')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/createcandidate.html")
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        response = self.client.post(reverse('updatecandidate', kwargs={'pk': cand.id}), 
            {'name': 'The Catcher in the Rye', 'phone': '235' , 'email' : 'as@g.com', 'previouscompany' : 'fs',
            'noticeperiod' : '20', 'resume' : 'reg.jpg' , 'datecreated' : timezone.now()
            })
        self.assertEqual(response.status_code, 302)
        cand.refresh_from_db()
        self.assertEqual(cand.phone, '235')

    def test_updatecandidatepage(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        response = self.client.get(reverse('updatecandidate', kwargs={'pk': cand.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/createcandidate.html")

class ViewsupdateInterviewer(TestCase):
    def test_updateinterviewer(self):
        response = self.client.get('/createinterviewer')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/createinterviewer.html")
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        response = self.client.post(reverse('updateinterviewer', kwargs={'pk': inter.id}), 
            {'name': 'The Catcher in the Rye', 'phone': '235' , 'email' : 'as@g.com', 'sapid' : '1421422', 'datecreated' : timezone.now()
            })
        self.assertEqual(response.status_code, 302)
        inter.refresh_from_db()
        self.assertEqual(inter.phone, '235')

    def test_updateinterviewerpage(self):
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        response = self.client.get(reverse('updateinterviewer', kwargs={'pk': inter.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/createinterviewer.html")

class ViewsdeleteInterviewer(TestCase):
    def test_deleteinterviewer(self):
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        response = self.client.post(reverse('deleteinterviewer', kwargs={'pk': inter.id}))
        self.assertEqual(response.status_code, 302)

    def test_deleteinterviewerpage(self):
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        response = self.client.get(reverse('deleteinterviewer', kwargs={'pk': inter.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/deleteinterviewer.html")

class ViewsdeleteCandidate(TestCase):
    def test_deletecandidate(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        response = self.client.post(reverse('deletecandidate', kwargs={'pk': cand.id}))
        self.assertEqual(response.status_code, 302)

    def test_deleteCandidatepage(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        response = self.client.get(reverse('deletecandidate', kwargs={'pk': cand.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/deletecandidate.html")

class ViewsdeleteSchedule(TestCase):
    def test_deleteSchedule(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        sch = Schedule.objects.create(candidate = cand, ipanel = inter, interviewdate = '2020-12-12', interviewtime = timezone.now())
        response = self.client.post(reverse('deleteschedule', kwargs={'pk': sch.id}))
        self.assertEqual(response.status_code, 302)
    def test_deleteSchedulepage(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        sch = Schedule.objects.create(candidate = cand, ipanel = inter, interviewdate = '2020-12-12', interviewtime = timezone.now())
        response = self.client.get(reverse('deleteschedule', kwargs={'pk': sch.id}))
        self.assertEqual(response.status_code, 200)

class Viewsupdateschedule(TestCase):
    #def test_updateschedule(self):
        #cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        #inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        #sch = Schedule.objects.create(candidate = cand, ipanel = inter, interviewdate = '2020-12-12',
        #interviewtime = timezone.now(), interviewname = 'IBM', interviewtype = 'Teams', position = 'Tester', status = 'Selected', remarks = 'good')
        #res1 = self.client.post(reverse('updateschedule', kwargs={'pk': sch.id}),
        #{'candidate': '',
        # 'ipanel': '' , 
        #'interviewdate' : '2020-10-10', 
        #'interviewtime' : timezone.now(),
        #'interviewname' : '', 
        #'interviewtype' : '',
        # 'position' : '',
        #  'status' : '', 
        #  'remarks' : ''})
        #self.assertRedirects(res1, 'home')
        #sch.refresh_from_db()
        #self.assertEqual(sch.interviewdate, '2020-10-10')

    def test_updateschedulepage(self):
        cand = Candidate.objects.create(name = "testcandidatename", phone = "1234", datecreated = timezone.now())
        inter = Interviewer.objects.create(name = "testinterviewername", phone = "1234", datecreated = timezone.now())
        sch = Schedule.objects.create(candidate = cand, ipanel = inter, interviewdate = '2020-12-12', interviewtime = timezone.now())
        response = self.client.get(reverse('updateschedule', kwargs={'pk': sch.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "interview/createschedule.html")