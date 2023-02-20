from django.db import models

class Tank(models.Model):
  tankname = models.CharField(max_length=255)
  nationality = models.CharField(max_length=255)
  crewmates_num = models.IntegerField(null=True)
  turret = models.BooleanField(null=True)

  def __str__(self): #to change the names of the tank objects on the admin page
    return f"{self.tankname} ({self.nationality})"
