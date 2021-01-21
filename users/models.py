from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
    name=models.CharField(max_length=30,verbose_name='Poll Name')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Author')
    text = models.TextField(max_length=300,verbose_name='Description')
    date = models.DateTimeField(default=timezone.now())
    option1 = models.TextField(max_length=500,verbose_name='Option 1')
    option2 = models.TextField(max_length=500,verbose_name='Option 2')
    option3 = models.TextField(max_length=500,verbose_name='Option 3')
    option4 = models.TextField(max_length=500,verbose_name='Option 4')
    is_anon = models.BooleanField(default=False,verbose_name='Anonymous Poll') # If Author wants to be anonymous
    count1 = models.PositiveIntegerField(default=0)
    count2 = models.PositiveIntegerField(default=0)
    count3 = models.PositiveIntegerField(default=0)
    count4 = models.PositiveIntegerField(default=0)
    

