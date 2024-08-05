from django.db import models
from django.utils.translation import gettext_lazy as _


class Housing(models.Model):
    HOUSING_CHOICES = [
        ('H', _('Haus')),
        ('A', _('Apartment')),
        ('O', _('Office')),
        ('H', _('Hall')),
        ('L', _('Land plot')),
    ]
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), )
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    rooms = models.IntegerField(_('Rooms'), )
    type = models.CharField(_('Type'), max_length=50, choices=HOUSING_CHOICES)

    def __str__(self):
        return self.name


class Address(models.Model):
    country = models.CharField(_('Country'), max_length=25)
    city = models.CharField(_('City'), max_length=20)
    street = models.CharField(_('Street'), max_length=100)
    house_number = models.CharField(_('Haus'), max_length=5)
    postal_code = models.IntegerField(_('Post'), max_length=8)
    object = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='addresses', verbose_name=_('Object'), blank=True, null=True)

    def __str__(self):
        return f'{self.street}, {self.house_number}, {self.postal_code} {self.city}, {self.country}'


