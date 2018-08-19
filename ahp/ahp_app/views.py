from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.core import urlresolvers
from django.contrib import messages
import datetime

from .models import SubCriteria, Bid, Criteria, Contractor
from .forms import ResponseForm, BidForm, BidCriteriaForm, BidSubCriteriaForm


class CreateContractor(PermissionRequiredMixin, generic.CreateView):
    model = Contractor
    fields = '__all__'
    permission_required = ['bid.admin', ]
    template_name = 'ahp_app/new_contractor.html'

    def get_success_url(self):
        return reverse_lazy('contractors')


class ContractorList(PermissionRequiredMixin, generic.ListView):
    model = Contractor
    template_name = 'ahp_app/contractors.html'
    permission_required = ['bid.admin', ]
    context_object_name = 'contractors'


class CreateBid(PermissionRequiredMixin, generic.CreateView):
    model = Bid
    form_class = BidForm
    permission_required = ['bid.admin', ]
    context_object_name = 'bid'
    template_name = 'ahp_app/new.html'

    def get_success_url(self):
        return reverse_lazy('bids')

    def form_valid(self, form):
        bid = form.save()
        key = bid.pk
        bid = get_object_or_404(Bid, pk=key)
        bid.save()
        return redirect(bid.get_add_criteria_url())


class ActivateBid(PermissionRequiredMixin, generic.UpdateView):
    model = Bid
    fields = ['activated', ]
    permission_required = ['bid.admin', ]
    context_object_name = 'bid'
    template_name = 'ahp_app/update.html'

    def get_success_url(self):
        return reverse_lazy('bids')


class CloseBid(PermissionRequiredMixin, generic.UpdateView):
    model = Bid
    fields = ['closed', ]
    permission_required = ['bid.admin', ]
    context_object_name = 'bid'
    template_name = 'ahp_app/update.html'

    def get_success_url(self):
        return reverse_lazy('bids')


class UpdateCriteria(PermissionRequiredMixin, generic.UpdateView):
    model = Bid
    form_class = BidCriteriaForm
    permission_required = ['bid.admin', ]
    context_object_name = 'bid'
    template_name = 'ahp_app/update.html'

    def get_success_url(self):
        return reverse_lazy('bids')

    def form_valid(self, form):
        bid = form.save()
        key = bid.pk
        bid = get_object_or_404(Bid, pk=key)
        criteria_list = bid.temp_criteria
        print(criteria_list)
        # criteria_list = criteria_list.split(',')
        # for c in criteria_list:
        #     crit = Criteria(name=c, survey=bid)
        #     crit.save()

        # bid.temp_criteria = ''
        # bid.save()
        # criteria = self.request.GET.get('id_temp_criteria')
        return redirect(self.get_success_url())


class UpdateSubCriteria(PermissionRequiredMixin, generic.UpdateView):
    model = Bid
    form_class = BidSubCriteriaForm
    permission_required = ['bid.admin', ]
    context_object_name = 'bid'
    template_name = 'ahp_app/update.html'

    def get_success_url(self):
        return reverse_lazy('bids')

    def form_valid(self, form):
        bid = form.save()
        key = bid.pk
        bid = get_object_or_404(Bid, pk=key)
        bid.save()
        subCrit = SubCriteria(text=bid.text, required=bid.required, category=bid.category,
                              question_type=bid.question_type, choices=bid.choices, survey=bid)
        subCrit.save()
        bid.text = ''
        bid.category = None
        bid.required = True
        bid.question_type = 'text'
        bid.choices = None
        bid.save()
        # criteria = self.request.GET.get('id_temp_criteria')
        return redirect(self.get_success_url())


def adminBidList(request):
    # bids = Bid.objects.all()
    bids = get_list_or_404(Bid)
    data = {
        'bids': bids,
    }
    return render(request, 'ahp_app/admin_list.html', data)


def bidList(request):
    bids = Bid.objects.filter(activated=True).filter(closed=False)
    # bids = bids.filter(closed=False)
    data = {
        'bids': bids,
    }
    return render(request, 'bids.html', data)


def BidDetail(request, pk):
    survey = Bid.objects.get(pk=pk)
    category_items = Criteria.objects.filter(survey=survey)
    categories = [c.name for c in category_items]
    print('criteria for this bid:')
    print(categories)
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save()
            return HttpResponseRedirect("/confirm/%s" % response.interview_uuid)
    else:
        form = ResponseForm(survey=survey)
        print(form)
        # TODO sort by category
    return render(request, 'survey.html', {'response_form': form, 'survey': survey, 'categories': categories})


def Confirm(request, pk):
    # email = settings.support_email
    email = 'danielale9291@gmail.com'
    uuid = 's'
    return render(request, 'confirm.html', {'uuid': uuid, "email": email})


def privacy(request):
    return render(request, 'privacy.html')

# Create your views here.


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('password-changed')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


class HomeView(View):
    """ This is a help docstring """

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class UpdatePassword(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['password', 'password1']
    template_name = 'registration/change_password.html'

    def get_success_url(self):
        return reverse_lazy('password-changed')


class PasswordChangedOk(LoginRequiredMixin, View):
    """ This is a help docstring """

    def get(self, request, *args, **kwargs):
        return render(request, 'registration/changed.html', {})
