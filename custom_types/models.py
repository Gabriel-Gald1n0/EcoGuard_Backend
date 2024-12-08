from django.db import models

class Custom_Type(models.Model):
    TYPES_CHOICES = [
        ("Water", "Water"),
        ("Soil", "Soil"),
        ("Air", "Air"),
    ]
    
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=55, choices=TYPES_CHOICES, default="Water")
    
    def __str__(self):
        return self.get_type_display()
