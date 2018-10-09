from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models


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

YES_NO_OPTIONS = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)
# Create your models here.


class FinancialStability(models.Model):
    contractor = models.ForeignKey(
        "Contractor", verbose_name="Choose Contractor", on_delete=models.CASCADE)
    soundness = models.FileField(
        upload_to='soundness/', null=True,  verbose_name="Financial Soundness")
    credit_rating = models.FileField(
        upload_to='credit_rating', null=True,  verbose_name="Financial Credit Rating")
    banking_bonding = models.FileField(
        upload_to='banking_bonding/', null=True, verbose_name="Financial Arrangements and Bonding")
    status = models.FileField(
        upload_to='status/', null=True, verbose_name="Financial Status")
    liquidity = models.FileField(
        upload_to='liquidity/', null=True, verbose_name="Financial Liquidity")

    def __str__(self):
        return self.contractor.name


class TechnicalCapability(models.Model):
    contractor = models.ForeignKey(
        "Contractor", verbose_name="Choose Contractor", on_delete=models.CASCADE)
    experience = models.FileField(
        upload_to="experience/", null=True, verbose_name="Experience of Technical Personnels")
    labour = models.FileField(
        upload_to="labour/", null=True, verbose_name="Labour and Equipment")
    qualification = models.FileField(
        upload_to="qualification/", null=True, verbose_name="Qualification of Personnels")
    ability = models.FileField(
        upload_to="ability/", null=True, verbose_name="Ability of Personnels")

    def __str__(self):
        return self.contractor.name


class PastPerformance(models.Model):
    contractor = models.ForeignKey(
        "Contractor", verbose_name="Choose Contractor", on_delete=models.CASCADE)
    quality = models.FileField(upload_to="quality/", null=True,
                               verbose_name="Quality Level of Project Performance")
    completedTime = models.FileField(
        upload_to="completionTime/", null=True, verbose_name="Projects Completed on Time")
    completedBudjet = models.FileField(
        upload_to="completedBudjet/", null=True, verbose_name="Projects Completed on Budget")

    def __str__(self):
        return self.contractor.name


class OccupationalHS(models.Model):
    contractor = models.ForeignKey(
        "Contractor", verbose_name="Choose Contractor", on_delete=models.CASCADE)
    healthSafety = models.FileField(
        upload_to="healthSafety/", null=True, verbose_name="Health and Safety Performance Report")
    safety = models.FileField(upload_to="safety/", null=True,
                              verbose_name="Occupational Safety and Health Administration Procedures")
    generalAssessment = models.FileField(
        upload_to="generalAssessment/", null=True, verbose_name="General Assessment of Safety Attitudes")

    def __str__(self):
        return self.contractor.name


class ManagementCapability(models.Model):
    contractor = models.ForeignKey(
        "Contractor", verbose_name="Choose Contractor", on_delete=models.CASCADE)
    qualityPolicy = models.FileField(
        upload_to="qualityPolicy/", null=True, verbose_name="Quality Policy")
    projectManagement = models.FileField(
        upload_to="projectManagement/", null=True, verbose_name="Project Management Organization")
    culture = models.FileField(
        upload_to="culture/", null=True, verbose_name="Organizational Culture")
    knowledge = models.FileField(
        upload_to="knowledge/", null=True, verbose_name="Management Knowledge")

    def __str__(self):
        return self.contractor.name


class Reputation(models.Model):
    contractor = models.ForeignKey(
        "Contractor", verbose_name="Choose Contractor", on_delete=models.CASCADE)
    failures = models.FileField(
        upload_to="failures/", null=True, verbose_name="Past Failures")
    timeInBusiness = models.FileField(
        upload_to="timeInBusiness/", null=True, verbose_name="Length of time in Business")
    pastOwner = models.FileField(
        upload_to="pastOwner/", null=True, verbose_name="Past Owner / Contractor Relationship")
    relationships = models.FileField(
        upload_to="relationships/", null=True, verbose_name="Other Relationships")

    def __str__(self):
        return self.contractor.name


class Experience(models.Model):
    contractor = models.ForeignKey(
        "Contractor", verbose_name="Choose Contractor", on_delete=models.CASCADE)
    projectType = models.FileField(
        upload_to="projectType/", null=True, verbose_name="Type of Past Projects Completed")
    projectSize = models.FileField(
        upload_to="projectSize/", null=True, verbose_name="Size of Past Projects Completed")
    numProject = models.FileField(
        upload_to="numProject/", null=True, verbose_name="Number of Past Projects Completed")
    localAreaExperience = models.FileField(
        upload_to="localAreaExperience/", null=True, verbose_name="Experience in Local Area")

    def __str__(self):
        return self.contractor.name


class Contractor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Business name')
    address = models.CharField(max_length=100, verbose_name='Address')
    phone = models.CharField(max_length=11, verbose_name='Phone number')
    email = models.EmailField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contractor-detail', kwargs={'pk': self.pk})


class Bid(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    activated = models.CharField(choices=YES_NO_OPTIONS, null=True,
                                 verbose_name='Activate Bid for Decision Makers', max_length=50)
    closed = models.BooleanField(default=False, verbose_name='Close Bid')
    contractors = models.ManyToManyField(Contractor)

    class Meta:
        permissions = (
            ('admin', 'admin'),
            ('decision_maker', 'decision_maker'),
        )

    def __str__(self):
        return self.name

    def get_activate_url(self):
        return reverse('activate-bid', kwargs={'pk': self.pk})

    def get_close_url(self):
        return reverse('close-bid', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('bid-detail', kwargs={'pk': self.pk})


class DecisionMaker(models.Model):
    name = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Response(models.Model):
    positive = models.CharField(null=True,
                                max_length=20, choices=POSITIVE_RESPONSE_OPTIONS)
    negative = models.CharField(null=True,
                                max_length=20, choices=REVERSE_RESPONSE_OPTIONS)


class FinancialStabilityRating(models.Model):
    bid_response = models.ForeignKey(
        "BidResponse", on_delete=models.CASCADE, null=True)
    soundness_positive = models.CharField(null=True, verbose_name="Financial Soundness",
                                          max_length=20, choices=POSITIVE_RESPONSE_OPTIONS)
    soundness_reverse = models.CharField(null=True, verbose_name="Financial Soundness - Reverse",
                                         max_length=20, choices=REVERSE_RESPONSE_OPTIONS)
    credit_rating_positive = models.CharField(null=True, verbose_name="Financial Credit Rating",
                                              max_length=20, choices=POSITIVE_RESPONSE_OPTIONS)
    credit_rating_reverse = models.CharField(null=True, verbose_name="Financial Credit Rating - Reverse",
                                             max_length=20, choices=REVERSE_RESPONSE_OPTIONS)
    banking_bonding_positive = models.CharField(null=True, verbose_name="Financial Arrangements and Bonding",
                                                max_length=20, choices=POSITIVE_RESPONSE_OPTIONS)
    banking_bonding_reverse = models.CharField(null=True, verbose_name="Financial Arrangements and Bonding - Reverse",
                                               max_length=20, choices=REVERSE_RESPONSE_OPTIONS)
    status_positive = models.CharField(null=True, verbose_name="Financial Status",
                                       max_length=20, choices=POSITIVE_RESPONSE_OPTIONS)
    status_reverse = models.CharField(null=True, verbose_name="Financial Status - Reverse",
                                      max_length=20, choices=REVERSE_RESPONSE_OPTIONS)
    liquidity_positive = models.CharField(null=True, verbose_name="Financial Liquidity",
                                          max_length=20, choices=POSITIVE_RESPONSE_OPTIONS)
    liquidity_reverse = models.CharField(null=True, verbose_name="Financial Liquidity - Reverse",
                                         max_length=20, choices=REVERSE_RESPONSE_OPTIONS)

    def __str__(self):
        return self.bid_response


class BidResponse(models.Model):
    decision_maker = models.ForeignKey(
        User, null=True, verbose_name="Decision Maker", on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, verbose_name="Bid",
                            on_delete=models.CASCADE)
    remarks = models.CharField(verbose_name="My Response", max_length=50)
    contractor = models.ForeignKey("Contractor", on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1}'.format(self.bid.name, self.contractor.name)

    def get_rate_financial_url(self):
        return reverse('rate-financial', kwargs={'pk': self.pk})
