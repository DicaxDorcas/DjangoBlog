from django.db import models
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    content = models.TextField()
    def __unicode__(self):
        return self.title
    
class Comments(models.Model):
    topic = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    pub_date = models.DateTimeField('date posted', auto_now_add=True)
    content = models.TextField()
    def __unicode__(self):
        return self.topic
 
