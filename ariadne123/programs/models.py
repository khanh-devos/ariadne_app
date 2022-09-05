from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Program(models.Model):
    teacher = models.ForeignKey(User, related_name="programs",
                              on_delete=models.CASCADE,
                              null=True)
    
    subject = models.CharField(max_length=100)
    period = models.PositiveIntegerField(default=6)
    
    def __str__(self):
        return f'program {self.subject}'

class Book(models.Model):
    program = models.ForeignKey(Program, related_name="books",
                              on_delete=models.CASCADE,
                              null=True)
    
    title = models.CharField(max_length=100)
    pages = models.PositiveIntegerField(default=100)
    
    published_at = models.DateField(null=True, default=None)
    
    cover = models.FileField(default='static/images/addimage.png',
                            upload_to=f'static/images/')
    
    def __str__(self):
        return self.title