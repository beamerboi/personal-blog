from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='images/', default='images/default.jpg')
    summary = models.TextField()

    def snippet(self):
        return self.summary[:70]+'...'
    def __str__(self):
        return self.title
