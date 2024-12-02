from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    url = models.URLField(blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # Use a range like 1-100
