from django.db import models
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    language = models.CharField(max_length=100)
    url = models.URLField()
    def getStub(self):
        return self.content[:300]
    def __unicode__(self):
        return self.title

