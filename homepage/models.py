from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Calculation(models.Model):
  '''Just an example model: a log of all calculations made'''
  log_date = models.DateTimeField(auto_now_add=True)
  num1 = models.FloatField(blank=True, null=True)
  num2 = models.FloatField(blank=True, null=True)
  operation = models.CharField(max_length=20, blank=True, null=True)
  result = models.FloatField(blank=True, null=True)
  
  def __str__(self):
    return '%s %s %s = %s' % (self.num1, self.operation, self.num2, self.result)
    
  
  
# from polls import models as pmod
# questions = pmod.Question.objects.all()
# pmod.Question.objects.filter(question_text='This is the third question')
# q1 = pmod.Question.objects.get(id=2)
# .exclude()   you can chain them together