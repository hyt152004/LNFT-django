from django.db import models

# Create your models here.

class Record(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  day_note = models.CharField(max_length=250)

  


  def __str__(self):
    return (f"{self.first_name} {self.last_name}")
  

