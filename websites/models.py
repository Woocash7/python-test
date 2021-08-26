from django.db import models

# Create your models here.
class Website(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=200, blank=True, null=True)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey('WebsiteCategory', on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.url}'

class WebsiteCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

class WebPage(models.Model):
    website = models.ForeignKey('Website', on_delete=models.CASCADE)
    URL = models.URLField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.website.title} | {self.URL}'
