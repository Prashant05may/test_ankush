from django.db import models

class NewModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
