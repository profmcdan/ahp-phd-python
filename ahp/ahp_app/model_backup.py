from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import User
from djongo import models

POSITIVE_RESPONSE_OPTIONS = (
    ('1,1,1', 'Equally Preferred'),
    ('1,2,3', 'Equally to Moderately Preferred'),
    ('2,3,4', 'Moderately Preferred'),
    ('3,4,5', 'Moderately to Strongly Preferred'),
    ('4,5,6', 'Strongly Preferred'),
    ('5,6,7', 'Strongly to Very Strongly Preferred'),
    ('6,7,8', 'Very Strongly Preferred'),
    ('7,8,9', 'Very Strongly to Extremely Preferred'),
    ('8,9,9', 'Extremely Preferred'),
)

REVERSE_RESPONSE_OPTIONS = (
    ('1,1,1', 'Equally Preferred'),
    ('0.3333,0.5,1', 'Equally to Moderately Preferred'),
    ('0.25,0.3333,0.5', 'Moderately Preferred'),
    ('0.2, 0.25, 0.3333', 'Moderately to Strongly Preferred'),
    ('0.1667, 0.2, 0.25', 'Strongly Preferred'),
    ('0.1429, 0.1667, 0.2', 'Strongly to Very Strongly Preferred'),
    ('0.125, 0.1429, 0.1667', 'Very Strongly Preferred'),
    ('0.1111, 0.125, 0.1429', 'Very Strongly to Extremely Preferred'),
    ('0.1111, 0.1111, 0.125', 'Extremely Preferred'),
)

CRITERIA_OPTIONS = (
    ('Financial Stability', 'Financial Stability'),
    ('Technical Capability', 'Technical Capability'),
    ('Past Performance', 'Past Performance'),
    ('Occupational Health & Safety', 'Occupational Health & Safety'),
    ('Management Capability', 'Management Capability'),
    ('Reputation', 'Reputation'),
    ('Experience  in Similar Project', 'Experience in Similar Project'),
)
# Create your models here.


class Contractor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Business name')
    address = models.CharField(max_length=100, verbose_name='Address')
    phone = models.CharField(max_length=11, verbose_name='Phone number')
    email = models.EmailField()

    def __str__(self):
        return self.name


class FinancialStability(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    soundness = models.FileField(
        db_alias='soundness', collection_name='soundness', verbose_name="Financial Soundness")
    credit_rating = models.FileField(
        db_alias='credit_rating', collection_name='credit_rating', verbose_name="Financial Credit Rating")
    banking_bonding = models.FileField(db_alias='banking_bonding', collection_name='banking_bonding',
                                       verbose_name="Financial Arrangements and Bonding")
    status = models.FileField(db_alias='status', collection_name='status',
                              verbose_name="Financial Status")
    liquidity = models.FileField(
        db_alias='liquidity', collection_name='liquidity', verbose_name="Financial Liquidity")

    def __str__(self):
        return self.contractor.name


class TechnicalCapability(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    experience = models.FileField(
        upload_to="experience/", null=True, verbose_name="Experience of Technical Personnels")
    labour = models.FileField(
        upload_to="labour/", null=True, verbose_name="Labour and Equipment")
    qualification = models.FileField(
        upload_to="qualification/", null=True, verbose_name="Qualification of Personnels")
    ability = models.FileField(
        upload_to="ability/", null=True, verbose_name="Ability of Personnels")

    class Meta:
        abstract = False


class PastPerformance(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    quality = models.FileField(upload_to="quality/", null=True,
                               verbose_name="Quality Level of Project Performance")
    completedTime = models.FileField(
        upload_to="completionTime/", null=True, verbose_name="Projects Completed on Time")
    completedBudjet = models.FileField(
        upload_to="completedBudjet/", null=True, verbose_name="Projects Completed on Budget")

    class Meta:
        abstract = False


class OccupationalHS(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    healthSafety = models.FileField(
        upload_to="healthSafety/", null=True, verbose_name="Health and Safety Performance Report")
    safety = models.FileField(upload_to="safety/", null=True,
                              verbose_name="Occupational Safety and Health Administration Procedures")
    generalAssessment = models.FileField(
        upload_to="generalAssessment/", null=True, verbose_name="General Assessment of Safety Attitudes")

    class Meta:
        abstract = False


class ManagementCapability(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    qualityPolicy = models.FileField(
        upload_to="qualityPolicy/", null=True, verbose_name="Quality Policy")
    projectManagement = models.FileField(
        upload_to="projectManagement/", null=True, verbose_name="Project Management Organization")
    culture = models.FileField(
        upload_to="culture/", null=True, verbose_name="Organizational Culture")
    knowledge = models.FileField(
        upload_to="knowledge/", null=True, verbose_name="Management Knowledge")

    class Meta:
        abstract = False


class Reputation(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    failures = models.FileField(
        upload_to="failures/", null=True, verbose_name="Past Failures")
    timeInBusiness = models.FileField(
        upload_to="timeInBusiness/", null=True, verbose_name="Length of time in Business")
    pastOwner = models.FileField(
        upload_to="pastOwner/", null=True, verbose_name="Past Owner / Contractor Relationship")
    relationships = models.FileField(
        upload_to="relationships/", null=True, verbose_name="Other Relationships")

    class Meta:
        abstract = False


class Experience(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    projectType = models.FileField(
        upload_to="projectType/", null=True, verbose_name="Type of Past Projects Completed")
    projectSize = models.FileField(
        upload_to="projectSize/", null=True, verbose_name="Size of Past Projects Completed")
    numProject = models.FileField(
        upload_to="numProject/", null=True, verbose_name="Number of Past Projects Completed")
    localAreaExperience = models.FileField(
        upload_to="localAreaExperience/", null=True, verbose_name="Experience in Local Area")

    class Meta:
        abstract = False


class MainBid(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    mode_date = models.DateTimeField()
    activated = models.BooleanField(
        default=False, verbose_name='Activate Bid for Decision Makers')
    closed = models.BooleanField(default=False)
    contractors = models.ArrayReferenceField(
        to=Contractor, on_delete=models.CASCADE)
    financial = models.ArrayModelField(model_container=FinancialStability)
    technical = models.ArrayModelField(model_container=TechnicalCapability)
    past = models.ArrayModelField(model_container=PastPerformance)
    occupational = models.ArrayModelField(model_container=OccupationalHS)
    financial = models.ArrayModelField(model_container=FinancialStability)
    management = models.ArrayModelField(
        model_container=ManagementCapability)
    reputation = models.ArrayModelField(model_container=Reputation)
    experience = models.ArrayModelField(model_container=Experience)

    def __str__(self):
        return self.name


class Bid2(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    mode_date = models.DateTimeField()
    activated = models.BooleanField(
        default=False, verbose_name='Activate Bid for Decision Makers')
    closed = models.BooleanField(default=False)
    status = models.FileField(db_alias='status', collection_name='status',
                              verbose_name="Financial Status")
    liquidity = models.FileField(
        db_alias='liquidity', collection_name='liquidity', verbose_name="Financial Liquidity")

    def __str__(self):
        return self.name


class Criteria(models.Model):
    name = models.CharField(max_length=400)
    survey = models.ForeignKey(
        'Bid', on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return (self.name)

    def __str__(self):
        return (self.name)


def validate_list(value):
    '''takes a text value and verifies that there is at least one comma '''
    values = value.split(',')
    if len(values) < 2:
        raise ValidationError(
            "The selected field requires an associated list of choices. Choices must contain more than one item.")


class SubCriteria(models.Model):
    TEXT = 'text'
    RADIO = 'radio'
    SELECT = 'select'
    SELECT_MULTIPLE = 'select-multiple'
    INTEGER = 'integer'

    QUESTION_TYPES = (
        (TEXT, 'text'),
        (RADIO, 'radio'),
        (SELECT, 'select'),
        (SELECT_MULTIPLE, 'Select Multiple'),
        (INTEGER, 'integer'),
    )

    text = models.CharField(max_length=255, null=True)
    required = models.BooleanField(default=True)
    category = models.ForeignKey(
        Criteria, on_delete=models.SET_NULL, blank=True, null=True)
    survey = models.ForeignKey(
        'Bid', on_delete=models.SET_NULL, blank=True, null=True)
    question_type = models.CharField(
        max_length=200, choices=QUESTION_TYPES, default=TEXT)
    # the choices field is only used if the question type
    choices = models.TextField(blank=True, null=True,
                               help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .')

    def save(self, *args, **kwargs):
        if (self.question_type == SubCriteria.RADIO or self.question_type == SubCriteria.SELECT
                or self.question_type == SubCriteria.SELECT_MULTIPLE):
            validate_list(self.choices)
        super(SubCriteria, self).save(*args, **kwargs)

    def __str__(self):
        return self.text

    def get_choices(self):
        ''' parse the choices field and return a tuple formatted appropriately
        for the 'choices' argument of a form widget.'''
        choices = self.choices.split(',')
        choices_list = []
        for c in choices:
            c = c.strip()
            choices_list.append((c, c))
        choices_tuple = tuple(choices_list)
        return choices_tuple

    def __unicode__(self):
        return (self.text)


class Bid(models.Model):
    TEXT = 'text'
    RADIO = 'radio'
    SELECT = 'select'
    SELECT_MULTIPLE = 'select-multiple'
    INTEGER = 'integer'

    QUESTION_TYPES = (
        (TEXT, 'text'),
        (RADIO, 'radio'),
        (SELECT, 'select'),
        (SELECT_MULTIPLE, 'Select Multiple'),
        (INTEGER, 'integer'),
    )

    name = models.CharField(max_length=400)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    activated = models.BooleanField(
        default=False, verbose_name='Activate Bid for Decision Makers')
    closed = models.BooleanField(default=False)
    contractor = models.ManyToManyField(Contractor, null=True)

    # Criteria Temp
    temp_criteria = models.CharField(max_length=400, choices=CRITERIA_OPTIONS,
                                     null=True, verbose_name="Select the appropriate criteria")
    # Subcriteria Temp
    text = models.CharField(max_length=255, null=True)
    required = models.BooleanField(default=True)
    category = models.ForeignKey(
        Criteria, on_delete=models.SET_NULL, blank=True, null=True)
    question_type = models.CharField(
        max_length=200, choices=QUESTION_TYPES, default=TEXT)
    # the choices field is only used if the question type
    positive_response = models.CharField(max_length=100, choices=POSITIVE_RESPONSE_OPTIONS, blank=True, null=True,
                                         verbose_name="Postive Response")
    reverse_response = models.CharField(max_length=100, choices=REVERSE_RESPONSE_OPTIONS, blank=True, null=True,
                                        verbose_name="Reverse Response")
    choices = models.TextField(
        blank=True, null=True, help_text='if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .')

    class Meta:
        permissions = (
            ('admin', 'admin'),
        )

    def __unicode__(self):
        return (self.name)

    def __str__(self):
        return (self.name)

    def get_activate_url(self):
        return reverse('activate-bid', kwargs={'pk': self.pk})

    def get_close_url(self):
        return reverse('close-bid', kwargs={'pk': self.pk})

    def get_add_subcriteria_url(self):
        return reverse('add-sub-criteria', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('bid-detail', kwargs={'pk': self.pk})

    def get_add_criteria_url(self):
        return reverse('add-criteria', kwargs={'pk': self.pk})

    def questions(self):
        if self.pk:
            return SubCriteria.objects.filter(survey=self.pk)
        else:
            return None


class Response(models.Model):
    # a response object is just a collection of questions and answers with a
    # unique interview uuid
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(
        Bid, on_delete=models.SET_NULL, blank=True, null=True)
    decision_maker = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    comments = models.TextField(
        'Any additional Comments', blank=True, null=True)
    interview_uuid = models.CharField(
        "Interview unique identifier", max_length=36)

    def __unicode__(self):
        return ("response %s" % self.interview_uuid)


class AnswerBase(models.Model):
    question = models.ForeignKey(
        SubCriteria, on_delete=models.SET_NULL, blank=True, null=True)
    response = models.ForeignKey(
        Response, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# these type-specific answer models use a text field to allow for flexible
# field sizes depending on the actual question this answer corresponds to. any
# "required" attribute will be enforced by the form.


class AnswerText(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerRadio(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerSelect(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerSelectMultiple(AnswerBase):
    body = models.TextField(blank=True, null=True)


class AnswerInteger(AnswerBase):
    body = models.IntegerField(blank=True, null=True)
