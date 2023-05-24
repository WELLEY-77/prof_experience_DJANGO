from django.db import models

class CadExperience(models.Model):
    cadexperience_id = models.BigAutoField(primary_key=True)
    cadexperience_first_name = models.CharField(max_length=50)
    cadexperience_last_name = models.CharField(max_length=50)
    cadexperience_degree = models.CharField(max_length=2)


    def __str__(self):
        return self.cadexperience_first_name

