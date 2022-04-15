from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    name = models.CharField('Name', max_length=250)
    username = models.CharField('Username', max_length=250)
    number = models.IntegerField('Number', default=0)
    message = models.TextField('Message')
    date = models.DateTimeField('Time', default=timezone.now())


    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

    
    def __str__(self):
        return str(self.name) +  ' | ' + str(self.date)
