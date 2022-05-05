from django.db import models

from fido.models import ShortTextField, FidoModel
from identities.models import LegalEntity, User, Address

from workflows.functions import *


class DeclaredAsset(FidoModel):
    manufacturer = ShortTextField()
    model_number = ShortTextField()
    description = ShortTextField()
    unique_id = ShortTextField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, blank=True)
    location_description = ShortTextField()



class RoleInvitation(FidoModel):
    class RelationshipChoices(models.TextChoices):
        SPOUSE = "spouse"
        CHILD = "child"
        GRANDCHILD = "grandchild"
        GREAT_GRANDCHILD = "great-grandchild"
    onboarding_form = models.ForeignKey("workflows.TrustQuestionaire", on_delete=models.PROTECT)
    first_name = ShortTextField()
    middle_initial = ShortTextField()
    last_name = ShortTextField()
    
    citizenship_status = models.BooleanField()
    address =  models.ForeignKey(Address, on_delete=models.PROTECT)
    relationship = ShortTextField(choices=RelationshipChoices.choices)

    # one of
    below_age_of_25 = models.BooleanField()
    date_of_birth = models.DateField(null=True, blank=True)



class Gift(FidoModel):
    onboarding_form = models.ForeignKey("workflows.TrustQuestionaire", on_delete=models.PROTECT,)
    asset = models.ForeignKey(DeclaredAsset, on_delete=models.PROTECT, null=True, blank=True)
    beneficiary = models.ForeignKey(RoleInvitation, on_delete=models.PROTECT, null=True, blank=True)



class TrustQuestionaire(FidoModel):
    identity = models.ForeignKey(LegalEntity, on_delete=models.PROTECT)

    previously_married = models.BooleanField(null=True, blank=True)
    spouse = models.ForeignKey(RoleInvitation, on_delete=models.PROTECT, null=True, blank=True)

    do_you_have_children = models.BooleanField(null=True, blank=True)
    do_you_have_grandchildren = models.BooleanField(null=True, blank=True)
    do_you_have_great_grandchildren = models.BooleanField(null=True, blank=True)

    real_estate = models.BooleanField(null=True, blank=True)
    bank_accounts = models.BooleanField(null=True, blank=True)
    retirement_accounts = models.BooleanField(null=True, blank=True)
    brokerage_accounts = models.BooleanField(null=True, blank=True)
    stock = models.BooleanField(null=True, blank=True)
    warrants = models.BooleanField(null=True, blank=True)
    bonds = models.BooleanField(null=True, blank=True)
    stock_options = models.BooleanField(null=True, blank=True)
    mutual_funds = models.BooleanField(null=True, blank=True)
    reits = models.BooleanField(null=True, blank=True)
    vehicles = models.BooleanField(null=True, blank=True)
    notes_or_debt = models.BooleanField(null=True, blank=True)
    safe_deposit_boxes = models.BooleanField(null=True, blank=True)
    business_interests = models.BooleanField(null=True, blank=True)
    patents_or_copywrites = models.BooleanField(null=True, blank=True)
    precious_metals_or_stones = models.BooleanField(null=True, blank=True)
    valuable_art_furniture_antique_collectibles = models.BooleanField(null=True, blank=True)


    disinherit_anyone = models.BooleanField(null=True, blank=True)
    likely_to_contest_will = models.BooleanField(null=True, blank=True)
    governmental_assistance = models.BooleanField(null=True, blank=True)
    special_needs_disabilities_or_addictions = models.BooleanField(null=True, blank=True)
    nursing_home = models.BooleanField(null=True, blank=True)
    creditor_problems = models.BooleanField(null=True, blank=True)
    divorce_a_concern = models.BooleanField(null=True, blank=True)
    specific_family_concerns = models.BooleanField(null=True, blank=True)


    continuing_obligations_from_divorce = models.BooleanField(null=True, blank=True)
    prenuptial_or_postnuptial_agreement = models.BooleanField(null=True, blank=True)
    gift_tax_returns = models.BooleanField(null=True, blank=True)
    oil_gas_mineral_rights = models.BooleanField(null=True, blank=True)
    water_rights = models.BooleanField(null=True, blank=True)
    timeshare_vacation_home = models.BooleanField(null=True, blank=True)
    family_business = models.BooleanField(null=True, blank=True)
    beneficiary_of_existing_trust = models.BooleanField(null=True, blank=True)
    combined_estate_over_20m = models.BooleanField(null=True, blank=True)
    long_temr_care_policy = models.BooleanField(null=True, blank=True)

    is_there_beneficiary_assign_asset = models.BooleanField(null=True, blank=True)
    is_there_beneficiary_assign_dollar = models.BooleanField(null=True, blank=True)

