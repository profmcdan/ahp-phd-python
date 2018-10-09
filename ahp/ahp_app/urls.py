from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from django.contrib.auth import login, logout

urlpatterns = [
    path('', views.HomeView.as_view(), name='root'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('password/', views.change_password, name='change_password'),
    path('password-ok/', views.PasswordChangedOk.as_view(), name='password-changed'),

    path('bid/', views.bidList, name='bids'),
    path('admin-view/', views.adminBidList, name='admin-views'),
    path('new-bid/', views.CreateBid.as_view(), name='new-bid'),
    #     path('bid/<int:pk>/add-criteria/',
    #          views.UpdateCriteria.as_view(), name='add-criteria'),
    #     path('bid/<int:pk>/add-subcriteria/',
    #          views.UpdateSubCriteria.as_view(), name='add-sub-criteria'),
    path('bid/<int:pk>', views.bid_detail, name='bid-detail'),
    path('bid/<int:pk>/activate/', views.ActivateBid.as_view(), name='activate-bid'),
    path('bid/<int:pk>/close/', views.ActivateBid.as_view(), name='close-bid'),
    path('confirm/<int:pk>/', views.confirm, name='confirmation'),
    path('privacy/', views.privacy, name='privacy_statement'),
    path('contractors/', views.ContractorList.as_view(), name='contractors'),
    path('new-contractor/', views.CreateContractor.as_view(), name='new-contractor'),
    path('contractor/<int:pk>/', views.get_contractor, name='contractor-detail'),

    path('rate-bid/', views.RateBid.as_view(), name='create-new-rating'),
    path('rate/<int:pk>/financial/',
         views.RateBidFinancial.as_view(), name='rate-financial'),
    path('fin-form/', views.fin_form, name='fin-form'),
    path('tech-form/', views.tech_form, name='tech-form'),
    path('past-perf/', views.past_performance_form, name='past-perf'),




]
