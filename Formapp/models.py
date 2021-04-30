from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length = 200, null = True,blank=True)
    password = models.CharField(max_length = 200, null = True,blank=True)
    email = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
