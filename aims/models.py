from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manuscript(models.Model):
    STATUS_CHOICES = [
        ('submitted', '제출됨'),
        ('under_review', '심사 중'),
        ('accepted', '승인됨'),
        ('rejected', '거절됨'),
    ]

    title = models.CharField(max_length=255)
    abstract = models.TextField()
    file = models.FileField(upload_to='manuscripts/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    submitted_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class ReviewerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise_keywords = models.TextField(help_text="Comma-separated keywords")
    publications = models.TextField()

class ManuscriptStatusHistory(models.Model):
    manuscript = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)