from django.db import models

from fido.models import ShortTextField, FidoModel
from identities.models import Identity, User

from workflows.functions import *


class Template(FidoModel):
    functions = TemplateF
    template_name = ShortTextField(max_length=200)
    is_live = models.BooleanField()


class TemplateRole(FidoModel):
    class RoleChoices(models.TextChoices):
        CLAIMABLE = "claimable"
        KNOWN_USERS = "known_users"
    functions = TemplateRoleF
    role_name = ShortTextField(max_length=200)
    role_type = ShortTextField(choices=RoleChoices.choices)
    role_choices = models.ManyToManyField(User)


class TemplateSection(FidoModel):
    functions = TemplateSectionF
    template = models.ForeignKey(Template, on_delete=models.PROTECT)
    position = models.IntegerField()
    section_name = ShortTextField(max_length=200)
    assignee_role = models.ForeignKey(TemplateRole, on_delete=models.PROTECT)


class TemplateQuestion(FidoModel):
    class QuestionChoices(models.TextChoices):
        CHECKBOX = "checkbox"
        MULTIPLE = "multiple"
        FREEFORM = "freeform"
        SIGNATURE = "signature"
    functions = TemplateQuestionF
    question_name = ShortTextField(max_length=200)
    question_type = ShortTextField(choices=QuestionChoices.choices)
    position = models.IntegerField()


class TemplateChoice(FidoModel):
    functions = TemplateChoiceF
    question = models.ForeignKey(TemplateQuestion, on_delete=models.PROTECT)
    choice_text = models.TextField()


class Intake(FidoModel):
    functions = IntakeF
    template = models.ForeignKey(Template, on_delete=models.PROTECT)


class IntakeRoleInvitation(FidoModel):
    functions = IntakeRoleInvitationF
    intake = models.ForeignKey(Intake, on_delete=models.PROTECT)
    role = models.ForeignKey(TemplateRole, on_delete=models.PROTECT)
    invite_name = ShortTextField(max_length=200)
    invite_email = models.EmailField(max_length=512)
    claimed_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)


class IntakeSection(FidoModel):
    functions = IntakeSectionF
    template_section = models.ForeignKey(TemplateSection, on_delete=models.PROTECT)
    assignees = models.ManyToManyField(User)


class IntakeResponse(FidoModel):
    functions = IntakeResponseF
    template_question = models.ForeignKey(TemplateQuestion, on_delete=models.PROTECT)
    selection = models.ForeignKey(TemplateChoice, on_delete=models.PROTECT, null=True, blank=True)
    data = models.TextField()