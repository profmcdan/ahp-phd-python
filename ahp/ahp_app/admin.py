
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import (Bid, Contractor,
                     DecisionMaker, BidResponse, FinancialStability, TechnicalCapability, PastPerformance, OccupationalHS, ManagementCapability, Reputation, Experience, FinancialStabilityRating)

admin.site.register([Bid, Contractor,
                     DecisionMaker, BidResponse, FinancialStability, TechnicalCapability, PastPerformance, OccupationalHS, ManagementCapability, Reputation, Experience, FinancialStabilityRating])
