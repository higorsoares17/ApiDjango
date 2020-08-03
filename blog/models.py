from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('publish','publish')
    )
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250) #https://site.com/noticias/campeonato-brasileiro-2020/01/02/2020
    author  = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create  = models.DateTimeField(auto_now_add=True)
    alter   = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,
                               choices=STATUS,
                               default='draft')
    
    
    class Meta:
        ordering = ('publish',)
    
    def __str__ (self):
        return '{} - {}'.format(self.title,self.slug)
# Create your models here.
