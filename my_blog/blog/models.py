from django.db import models

# Create your models here.
class Habitat(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
        





















