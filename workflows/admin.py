from django.contrib import admin
from workflows.models import *


# Register your models here.
@admin.register(TrustQuestionaire)
class TrustQuestionaireAdmin(admin.ModelAdmin):
    pass


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    pass



