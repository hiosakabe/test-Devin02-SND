from django.db import models

class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class UsageExample(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    code_example = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
