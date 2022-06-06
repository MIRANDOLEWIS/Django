from django.db import models

# Create your models here.
class LinkInfo(models.Model):
    mainlink = models.CharField(max_length=10000)
    linkid = models.CharField(max_length=10)

    def __str__(self):
        return self.linkid 