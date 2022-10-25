from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Not Active', 'Not Active'),
    )
    name = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, null=True)
    empNum = models.IntegerField(null=True)
    designation  = models.CharField(max_length=200, null=True)
    team  = models.CharField(max_length=200, null=True)
    manager  = models.CharField(max_length=200, null=True)
    location  = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    #profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    dor = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    PROJECTSTATUS = (
        ('Exists', 'Exists'),
        ('Not Exists', 'Not Exists'),
    )
    name = models.CharField(max_length=200, null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    country = models.CharField(max_length=200, null=True)
    platform = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    handled = models.ManyToManyField(Employee)
    status = models.CharField(max_length=200, null=True, choices=PROJECTSTATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tracker(models.Model):
    JOBSTATUS = (
        ('Completed','Completed'),
        ('WIP','WIP'),
    )
    employee = models.CharField(max_length=200, null=True)
    client = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)
    activity = models.CharField(max_length=200, null=True)
    workedDate = models.DateField(null=True, blank=True)
    spentTimeHr = models.IntegerField(null=True, blank=True)
    spentTimeMin = models.IntegerField(null=True, blank=True)
    fileCount = models.SmallIntegerField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=JOBSTATUS)