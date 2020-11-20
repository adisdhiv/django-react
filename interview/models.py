from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length = 50, null = True, blank= True)
    phone = models.CharField(max_length = 50, null = True, blank= True)
    email = models.EmailField(max_length = 50, null = True, blank= True)
    previouscompany = models.CharField(max_length = 50, null = True, blank= True)
    noticeperiod = models.CharField(max_length = 50, null = True, blank= True)
    resume = models.FileField(null = True, blank= True)
    datecreated = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

class Interviewer(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    phone = models.CharField(max_length = 50, null = True, blank = True)
    email = models.EmailField(max_length = 50, null = True, blank = True)
    sapid = models.CharField(max_length = 8, null = True, blank = True)
    datecreated = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    STATUS = (
		('Selected', 'Selected'),
		('Rejected', 'Rejected'),
    )
    POSITION = (
		('Developer', 'Developer'),
		('Tester', 'Tester'),
        ('Devops', 'Devops'),
    )
    TYPE = (
		('Teams', 'Teams'),
		('Telephonic', 'Telephonic'),
    )
    INAME = (
		('HCLPanel1', 'HCLPanel1'),
		('HCLPanel2', 'HCLPanel2'),
        ('IBM', 'IBM'),
    )
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null = True)
    ipanel = models.ForeignKey(Interviewer, on_delete=models.SET_NULL, null = True)
    position = models.CharField(max_length = 50, null = True, choices = POSITION, blank = True)
    status = models.CharField(max_length = 50, null = True, choices = STATUS, blank = True)
    interviewname = models.CharField(max_length = 50, null = True, choices = INAME, blank = True)
    interviewtype = models.CharField(max_length = 50, null = True, choices = TYPE, blank = True)
    interviewdate = models.DateField(null = True)
    interviewtime = models.TimeField(null = True)
    remarks = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.candidate.name