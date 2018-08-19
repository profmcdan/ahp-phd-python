from .models import (SubCriteria, Criteria, Bid, Response, AnswerText, AnswerRadio,
                      AnswerSelect, AnswerInteger, AnswerSelectMultiple, Contractor)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class SubCriteriaInline(admin.TabularInline):
	model = SubCriteria
	ordering = ('category',)
	extra = 0


class CriteriaInline(admin.TabularInline):
	model = Criteria
	extra = 0


class BidAdmin(admin.ModelAdmin):
	inlines = [CriteriaInline, SubCriteriaInline]


class AnswerBaseInline(admin.StackedInline):
	fields = ('question', 'body')
	readonly_fields = ('question',)
	extra = 0


class AnswerTextInline(AnswerBaseInline):
	model = AnswerText


class AnswerRadioInline(AnswerBaseInline):
	model = AnswerRadio


class AnswerSelectInline(AnswerBaseInline):
	model = AnswerSelect


class AnswerSelectMultipleInline(AnswerBaseInline):
	model = AnswerSelectMultiple


class AnswerIntegerInline(AnswerBaseInline):
	model = AnswerInteger


class ResponseAdmin(admin.ModelAdmin):
	list_display = ('interview_uuid', 'decision_maker', 'created')
	inlines = [AnswerTextInline, AnswerRadioInline, AnswerSelectInline,
            AnswerSelectMultipleInline, AnswerIntegerInline]
	# specifies the order as well as which fields to act on
	readonly_fields = ('survey', 'created', 'updated', 'interview_uuid')


#admin.site.register(Question, QuestionInline)
#admin.site.register(Category, CategoryInline)
admin.site.register(Bid, BidAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Contractor)
