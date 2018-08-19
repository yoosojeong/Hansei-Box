from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

class Profile(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(_('Name of User'), blank=True, max_length=30)
    age = models.IntegerField(null=True)

    phone_number = models.CharField(
        max_length=20,
        #validators=[RegexValidator(r'^010[1-9]\d[6,7]$')],
    )

    def __str__(self):
        return self.name