# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
from django.contrib import admin
from django import forms

from django_admin_hstore_widget.forms import HStoreFormField
from models import Rider,Ride,Driver

class RiderAdminForm(forms.ModelForm):
    rider = HStoreFormField()
    soloRideHistory = HStoreFormField()
    class Meta:
       model = Rider
       exclude = ()

@admin.register(Rider)
class RiderlAdmin(admin.ModelAdmin):
    form = RiderAdminForm

class RideAdminForm(forms.ModelForm):
    flushedDrivers = HStoreFormField()
    class Meta:
       model = Ride
       exclude = ()

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    form = RideAdminForm

class DriverAdminForm(forms.ModelForm):
    adminCreditHistory = HStoreFormField()
    lastKnownLocation = HStoreFormField()
    redeemRequestHistory = HStoreFormField()
    referralTo = HStoreFormField()
    seats = HStoreFormField()
    soloExpressHistory = HStoreFormField()
    soloRideHistory = HStoreFormField()
    class Meta:
       model = Driver
       exclude = ()

@admin.register(Driver)
class RiderlAdmin(admin.ModelAdmin):
    form = DriverAdminForm

# Register your models here.
# admin.site.register(models.Riders)
