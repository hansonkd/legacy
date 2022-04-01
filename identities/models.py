from django.db import models
from localflavor.us.models import USStateField
from django_countries.fields import CountryField

from fido.models import ShortTextField

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Identity(models.Model):
    admin = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    legal_name = ShortTextField()
    tax_id = ShortTextField()


class Location(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.PROTECT)
    primary = models.BooleanField()

    address_1 = ShortTextField("address", max_length=128, null=True, blank=True)
    address_2 = ShortTextField("address cont'd", max_length=128, null=True, blank=True)

    city = ShortTextField("city", max_length=64, default="San Diego")
    state = USStateField("state", default="CA")
    zip_code = ShortTextField("zip code", max_length=10, default="92037")
    country = CountryField()

