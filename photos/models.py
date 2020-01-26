from django.db import models

class Photo(models.Model):

    caption = models.CharField(max_length = 255, verbose_name = u'Photo_Caption')
    status = models.CharField(max_length = 255, verbose_name = u'Photo_Status')
    url = models.CharField(max_length = 500, verbose_name = u'Photo_Url')
    changed_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ('changed_on', '-changed_on')
