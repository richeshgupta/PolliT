from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Poll(models.Model):
    name=models.CharField(max_length=30,verbose_name='Poll Name')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Author')
    text = RichTextField(blank=True,null=True,max_length=3000,verbose_name='Description')
    date = models.DateTimeField(default=timezone.now())
    option1 = models.TextField(max_length=500,verbose_name='Option 1')
    option2 = models.TextField(max_length=500,verbose_name='Option 2')
    option3 = models.TextField(max_length=500,verbose_name='Option 3')
    option4 = models.TextField(max_length=500,verbose_name='Option 4')
    is_anon = models.BooleanField(default=False,verbose_name='Anonymous Poll (Author will be hidden)') # If Author wants to be anonymous
    count1 = models.PositiveIntegerField(default=0)
    count2 = models.PositiveIntegerField(default=0)
    count3 = models.PositiveIntegerField(default=0)
    count4 = models.PositiveIntegerField(default=0)
    def get_absolute_url(self):
        return reverse('home')
    def __str__(self):
        return self.name + " : " + self.text