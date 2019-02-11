from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # class is key word to say you are defining an object, class name must always start with an uppercase, model.model means its a django model and should be saved in database 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link to another model 
    title = models.CharField(max_length=200)
    text = models.TextField() # attribute for long text feilds without char limits 
    created_date = models.DateTimeField(default=timezone.now) #date and time feilds
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #use lower cases to define function and underscores for spaces 
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title # returns a text string with a post title 