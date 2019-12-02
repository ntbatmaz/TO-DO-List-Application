
# todo/models.py
      
from django.db import models
# Create your models here.

# add this
class Todo(models.Model):
  completed = models.BooleanField(default=False)
  title = models.CharField(max_length=120)
  description = models.TextField()
  
      
  def __str__(self):
    return self.title