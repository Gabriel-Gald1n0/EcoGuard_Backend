from django.db import models
from regions.models import Region    

class Report(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    region = models.ForeignKey(
        Region, 
        on_delete=models.CASCADE
    )
    
