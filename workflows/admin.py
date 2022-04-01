from django.contrib import admin
from workflows.models import *


# Register your models here.
@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateRole)
class TemplateRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateSection)
class TemplateSectionAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateQuestion)
class TemplateQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateChoice)
class TemplateChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Intake)
class IntakeAdmin(admin.ModelAdmin):
    pass


@admin.register(IntakeSection)
class IntakeSectionAdmin(admin.ModelAdmin):
    pass


@admin.register(IntakeResponse)
class IntakeResponseAdmin(admin.ModelAdmin):
    pass

