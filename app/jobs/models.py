from django.db import models
import uuid
import datetime
from users.models import Profile
# Create your models here.

class Job(models.Model):
    STATUS_CHOICE = [
        ('applied','Applied'),
        ('phone','Phone Interview'),
        ('technical','Technical Interview'),
        ('offer','Offer'),
        ('rejected','Applied'),
        ('applied','Applied'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    apply_date = models.DateField()
    apply_platform = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=STATUS_CHOICE)
    job_post = models.CharField(max_length=200)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.owner.name} --> {self.company_name} --> {self.job_title}'

def _upload_path(instance, filename):
    return instance.get_upload_path(filename)

class Resume(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume_name = models.CharField(max_length=200)
    resume_file = models.FileField(upload_to=_upload_path)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.owner.id} --> {self.resume_name}'

    def get_upload_path(self, filename):
        return f'uploads/resumes/{self.owner.id}/{filename}'

    @property
    def getResumeCount(self):
        return self.resume_set.all().count()