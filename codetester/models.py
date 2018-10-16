from django.db import models

class Submission(models.Model):
    submission_code = models.CharField(max_length=20000)
    pub_date = models.DateTimeField('date published')
    score = models.IntegerField()
# Create your models here.
