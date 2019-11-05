from django.db import models

class search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=true)
