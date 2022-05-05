from django.contrib import admin
from identities.models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(LegalEntity)
class LegalEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass