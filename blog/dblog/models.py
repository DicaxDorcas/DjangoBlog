from django.db import models
from tagging.fields import TagField
from tagging.models import Tag
from django.template.defaultfilters import slugify
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    content = models.TextField()
    author = models.CharField(max_length=50)
    tags = TagField()

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)
    def get_tags(self):
        return Tag.objects.get_for_object(self)
    def getStub(self):
        return self.content[:300]
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
