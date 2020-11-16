# Standard Library
import csv
import os

# Django Library
from django.conf import settings
from django.db import models
from django.db.models import ProtectedError
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class PyFather(models.Model):
    active = models.BooleanField(default=True, blank=True, null=True)
    fc = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fm = models.DateTimeField(auto_now=True, blank=True, null=True)
    uc = models.IntegerField(null=True, blank=True)
    um = models.IntegerField(null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['pk']
        abstract = True

    def get_absolute_url(self):
        return reverse('{}:detail'.format(self._meta.object_name), kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        try:
            super().delete(*args, **kwargs)
            message = _("'The %(obj_name)s was deleted successfully.'") % {'obj_name': self._meta.verbose_name}
            return "messages.success(request, {})".format(message)
        except ProtectedError:
            message = _("'The %(obj_name)s cannot be deleted, certain information on system depends on this.'") % {'obj_name': self._meta.verbose_name}
            return "messages.error(request, {})".format(message)