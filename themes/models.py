from django.utils.translation import ugettext_lazy as _
from django.db import models

class Theme(models.Model):
    class_name = models.CharField(
        _(u'class'),
        max_length=100
        )

    class Meta:
        verbose_name = _(u'class')
        verbose_name_plural = _(u'classes')

    def __unicode__(self):
        return u"%s" % self.class_name
