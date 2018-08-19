from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='root'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('password/', views.change_password, name='change_password'),
    path('passwordok/', views.PasswordChangedOk.as_view(), name='password-changed'),

    path('bid/', views.bidList, name='bids'),
    path('admin-view/', views.adminBidList, name='admin-views'),
    path('new-bid/', views.CreateBid.as_view(), name='new-bid'),
    path('bid/<int:pk>/add-criteria/', views.UpdateCriteria.as_view(), name='add-criteria'),
    path('bid/<int:pk>/add-subcriteria/', views.UpdateSubCriteria.as_view(), name='add-sub-criteria'),
   	path('bid/<int:pk>', views.BidDetail, name='bid-detail'),
    path('bid/<int:pk>/activate/', views.ActivateBid.as_view(), name='activate-bid'),
    path('bid/<int:pk>/close/', views.ActivateBid.as_view(), name='close-bid'),
   	path('confirm/<int:pk>/', views.Confirm, name='confirmation'),
   	url(r'^privacy/$', views.privacy, name='privacy_statement'),
    path('contractors/', views.ContractorList.as_view(), name='contractors'),
    path('new-contractor/', views.CreateContractor.as_view(), name='new-contractor'),


   	# Uncomment the admin/doc line below to enable admin documentation:
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]
