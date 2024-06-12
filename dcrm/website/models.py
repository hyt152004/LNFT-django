from django.db import models

# Create your models here.

class Record(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=50)
  first_prompt = models.CharField(max_length=300)
  second_prompt = models.CharField(max_length=300)
  third_prompt = models.CharField(max_length=300)

  


  def __str__(self):
    # return (f"{self.first_name} {self.last_name}")
    return (f" ")
  

