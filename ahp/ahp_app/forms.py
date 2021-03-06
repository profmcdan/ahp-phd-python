from django import forms
from django.forms import models
from .models import (Bid, BidResponse, FinancialStabilityRating)
from django.utils.safestring import mark_safe
import uuid

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


class BidForm(models.ModelForm):
    class Meta:
        model = Bid
        fields = ['name', 'description', 'contractors', ]
        widgets = {
            'contractors': forms.SelectMultiple(attrs={'class': 'chosen-select'}),
        }


class PreRateBid(forms.ModelForm):
    class Meta:
        model = BidResponse
        fields = ['bid', 'contractor', 'remarks', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bid'].queryset = Bid.objects.filter(
            activated='Yes').filter(closed=False)


class RateFinancialStabilityForm(forms.ModelForm):
    class Meta:
        model = FinancialStabilityRating
        fields = ['soundness_positive', 'soundness_reverse', 'credit_rating_positive', 'credit_rating_reverse', 'banking_bonding_positive',
                  'banking_bonding_reverse', 'status_positive', 'status_reverse', 'liquidity_positive', 'liquidity_reverse']


class RateBidFinancialForm(forms.Form):
    soundness = forms.ChoiceField(choices=POSITIVE_RESPONSE_OPTIONS)
    soundness_reverse = forms.ChoiceField(choices=REVERSE_RESPONSE_OPTIONS)
    credit_rating = forms.ChoiceField(choices=POSITIVE_RESPONSE_OPTIONS)
    credit_rating_reverse = forms.ChoiceField(choices=REVERSE_RESPONSE_OPTIONS)
    banking_bonding = forms.ChoiceField(choices=POSITIVE_RESPONSE_OPTIONS)
    banking_bonding_reverse = forms.ChoiceField(
        choices=REVERSE_RESPONSE_OPTIONS)
    status = forms.ChoiceField(choices=POSITIVE_RESPONSE_OPTIONS)
    status_reverse = forms.ChoiceField(choices=REVERSE_RESPONSE_OPTIONS)
    liquidity = forms.ChoiceField(choices=POSITIVE_RESPONSE_OPTIONS)
    liquidity_reverse = forms.ChoiceField(choices=REVERSE_RESPONSE_OPTIONS)


# # blatantly stolen from
# # http://stackoverflow.com/questions/5935546/align-radio-buttons-horizontally-in-django-forms?rq=1


# # class HorizontalRadioRenderer(forms.RadioSelect.renderer):
# #   def render(self):
# #     return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

# class BidForm(models.ModelForm):
#     class Meta:
#         model = Bid
#         fields = ['name', 'description', 'contractor', ]
#         widgets = {
#             'contractor': forms.SelectMultiple(attrs={'class': 'chosen-select'}),
#         }


# class BidCriteriaForm(models.ModelForm):
#     class Meta:
#         model = Bid
#         fields = ['temp_criteria', ]
#         widgets = {
#             'temp_criteria': forms.SelectMultiple(),
#         }


# class BidSubCriteriaForm(models.ModelForm):
#     class Meta:
#         model = Bid
#         fields = ['category', 'text', 'required',
#                   'question_type', 'choices']

#     def __init__(self, *args, **kwargs):
#         super(BidSubCriteriaForm, self).__init__(*args, **kwargs)
#         self.fields['category'].queryset = Criteria.objects.filter(
#             survey=kwargs['instance'])


# class ResponseForm(models.ModelForm):
#     class Meta:
#         model = Response
#         fields = ('comments',)

#     def __init__(self, *args, **kwargs):
#         # expects a survey object to be passed in initially
#         survey = kwargs.pop('survey')
#         self.survey = survey
#         super(ResponseForm, self).__init__(*args, **kwargs)
#         self.uuid = uuid.uuid4().hex

#         # add a field for each survey question, corresponding to the question
#         # type as appropriate.
#         data = kwargs.get('data')
#         for q in survey.questions():
#             if q.question_type == SubCriteria.TEXT:
#                 self.fields["question_%d" % q.pk] = forms.CharField(label=q.text,
#                                                                     widget=forms.Textarea)
#             elif q.question_type == SubCriteria.RADIO:
#                 question_choices = q.get_choices()
#                 self.fields["question_%d" % q.pk] = forms.ChoiceField(label=q.text,
#                                                                       choices=question_choices)
#             elif q.question_type == SubCriteria.SELECT:
#                 question_choices = q.get_choices()
#                 # add an empty option at the top so that the user has to
#                 # explicitly select one of the options
#                 question_choices = tuple(
#                     [('', '-------------')]) + question_choices
#                 self.fields["question_%d" % q.pk] = forms.ChoiceField(label=q.text,
#                                                                       widget=forms.Select, choices=question_choices)
#             elif q.question_type == SubCriteria.SELECT_MULTIPLE:
#                 question_choices = q.get_choices()
#                 self.fields["question_%d" % q.pk] = forms.MultipleChoiceField(label=q.text,
#                                                                               widget=forms.CheckboxSelectMultiple, choices=question_choices)
#             elif q.question_type == SubCriteria.INTEGER:
#                 self.fields["question_%d" %
#                             q.pk] = forms.IntegerField(label=q.text)

#             # if the field is required, give it a corresponding css class.
#             if q.required:
#                 self.fields["question_%d" % q.pk].required = True
#                 self.fields["question_%d" %
#                             q.pk].widget.attrs["class"] = "required"
#             else:
#                 self.fields["question_%d" % q.pk].required = False

#             # add the category as a css class, and add it as a data attribute
#             # as well (this is used in the template to allow sorting the
#             # questions by category)
#             if q.category:
#                 classes = self.fields["question_%d" %
#                                       q.pk].widget.attrs.get("class")
#                 if classes:
#                     self.fields["question_%d" % q.pk].widget.attrs["class"] = classes + \
#                         (" cat_%s" % q.category.name)
#                 else:
#                     self.fields["question_%d" % q.pk].widget.attrs["class"] = (
#                         " cat_%s" % q.category.name)
#                 self.fields["question_%d" %
#                             q.pk].widget.attrs["category"] = q.category.name

#             # initialize the form field with values from a POST request, if any.
#             if data:
#                 self.fields["question_%d" %
#                             q.pk].initial = data.get('question_%d' % q.pk)

#     def save(self, commit=True):
#         # save the response object
#         response = super(ResponseForm, self).save(commit=False)
#         response.survey = self.survey
#         response.interview_uuid = self.uuid
#         response.save()

#         # create an answer object for each question and associate it with this
#         # response.
#         for field_name, field_value in self.cleaned_data.iteritems():
#             if field_name.startswith("question_"):
#                 # warning: this way of extracting the id is very fragile and
#                 # entirely dependent on the way the question_id is encoded in the
#                 # field name in the __init__ method of this form class.
#                 q_id = int(field_name.split("_")[1])
#                 q = SubCriteria.objects.get(pk=q_id)

#                 if q.question_type == SubCriteria.TEXT:
#                     a = AnswerText(question=q)
#                     a.body = field_value
#                 elif q.question_type == SubCriteria.RADIO:
#                     a = AnswerRadio(question=q)
#                     a.body = field_value
#                 elif q.question_type == SubCriteria.SELECT:
#                     a = AnswerSelect(question=q)
#                     a.body = field_value
#                 elif q.question_type == SubCriteria.SELECT_MULTIPLE:
#                     a = AnswerSelectMultiple(question=q)
#                     a.body = field_value
#                 elif q.question_type == SubCriteria.INTEGER:
#                     a = AnswerInteger(question=q)
#                     a.body = field_value
#                 print("creating answer to question {0} of type {1}".format(
#                     q_id, a.question.question_type))
#                 print(a.question.text)
#                 print('answer value:')
#                 print(field_value)
#                 a.response = response
#                 a.save()
#         return response
