from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=100)
    length_miles = models.FloatField()
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Park(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    

    def get_absolute_url(self):
        return reverse('park-detail', kwargs={'park_id': self.id})



class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    type = models.CharField(max_length=55, choices=[
        ('waterfall', 'Waterfall'),
        ('viewpoint', 'Viewpoint'),
        ('historical', 'Historical Site'),
        ('visitor_center', 'Visitor Center'),
        ('cave', 'Cave'),
        ('lake', 'Lake'),
        ('trailhead', 'Trailhead'),
        ('other', 'Other'), 
    ])
    park = models.ForeignKey(
        Park, 
        on_delete=models.CASCADE, 
        related_name='attractions',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('park-detail', kwargs={'park_id': self.id})



