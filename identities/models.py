from django.db import models
from localflavor.us.models import USStateField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from fido.models import ShortTextField

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone_number = PhoneNumberField()



class LegalEntity(models.Model):
    class EntityChoices(models.TextChoices):
        ORGANIZATION = "organization"
        PERSON = "person"
    entity_type = ShortTextField(choices=EntityChoices.choices)
    admin = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    legal_name = ShortTextField()
    first_name = ShortTextField()
    middle_initial = ShortTextField()
    last_name = ShortTextField()
    tax_id = ShortTextField()

    phone_number = PhoneNumberField()



class Address(models.Model):
    address_1 = ShortTextField("address", max_length=128, null=True, blank=True)
    address_2 = ShortTextField("address cont'd", max_length=128, null=True, blank=True)

    city = ShortTextField("city", max_length=64, default="San Diego")
    state = USStateField("state", default="CA")
    zip_code = ShortTextField("zip code", max_length=10, default="92037")
    country = CountryField()

