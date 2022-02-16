from django.db import models

# Create your models here.

class Client(models.Model):
    CHOOSE_SUBJECT = (
        ('Data Analysis','Data Analysis'),
        ('Web Development','Web Development'),
        ('Digital Marketing','Digital Marketing'),
        ('Others(Specify)','Others(Specify)')
    )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number = models.FloatField(max_length=50, null=True)
    choose_subject = models.CharField(max_length=200, null=True, choices=CHOOSE_SUBJECT)
    describe_project = models.CharField(max_length=200, null=True)
