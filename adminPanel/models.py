# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import HStoreField
from django.db import models
from django.db import connection
from django.db.models.signals import pre_migrate
from django.dispatch import receiver
import sys
from django.contrib.postgres.fields import ArrayField,JSONField,HStoreField
from adminPanel.choices import *
# sender is optional but will be called for every pre_migrate signal if removed
@receiver(pre_migrate, sender=sys.modules[__name__])
def setup_postgres_hstore(sender, **kwargs):
    """
    Always create PostgreSQL HSTORE extension if it doesn't already exist
    on the database before syncing the database.
    Requires PostgreSQL 9.1 or newer.
    """
    cursor = connection.cursor()
    cursor.execute("CREATE EXTENSION IF NOT EXISTS hstore")


class Rider(models.Model):
    id = models.CharField(primary_key = True,max_length = 255)
    phoneNumber = models.CharField(max_length = 255,unique = True)
    createdAt = models.DateTimeField(auto_now = False,auto_now_add = False)
    emailId = models.EmailField(null = True,blank = True)
    fcmToken = models.CharField(max_length = 255,null = True,blank = True)
    firstName = models.CharField(max_length = 255,null = True,blank = True)
    lastName = models.CharField(max_length = 255,null = True,blank = True)
    paymentPreference = models.CharField(max_length = 255,null = True,blank = True)
    picture = models.CharField(max_length = 255,null = True,blank = True)
    rating = models.FloatField(null = True,blank = True)
    referralMoney = models.FloatField(null = True,blank = True)
    referredBy = models.CharField(max_length = 255,null = True,blank = True)
    rider = HStoreField(blank = True,default = {"NA":"NA"})
    soloRideHistory = HStoreField(blank = True,default = {"NA":"NA"})
    soloExpressHistory = JSONField()
    state = models.CharField(max_length = 255,null = True,blank = True)
    status = models.CharField(max_length = 255,null = True,blank = True)
    walletId = models.CharField(max_length = 255,null = True,blank = True)
    def __str__(self):
        return self.id


class Ride(models.Model):
    id = models.CharField(primary_key = True,max_length = 255)
    cancelTime = models.DateTimeField(auto_now = False,auto_now_add = False)
    cancelType = models.CharField(max_length = 255,null = True,blank = True)
    destination = JSONField()
    destinationLocationEnglish = models.CharField(null = True,max_length = 255,blank = True)
    destinationLocationHindi = models.CharField(max_length = 255,null = True,blank = True)
    driverId = models.CharField(max_length = 255,null = True,blank = True)
    driverMobile = models.CharField(max_length = 255,null = True,blank = True)
    flushedDrivers = HStoreField()
    paymentMode = models.CharField(null = True,max_length = 255,blank = True)
    projectRideDistance = models.CharField(null = True,max_length = 255,blank = True)
    projectedPickupTime = models.CharField(null = True,max_length = 255,blank = True)
    projectRideCost = models.CharField(null = True,max_length = 255,blank = True)
    projectRideCostWithOffer = models.FloatField(null = True,blank=True)
    projectedRideTime = models.CharField(null = True,max_length = 255,blank = True)
    requestedTime = models.DateTimeField(auto_now=False,auto_now_add=False,blank = True)
    riderMobile = models.CharField(null = True,max_length = 255,blank = True)
    riderName = models.CharField(null = True,max_length = 255,blank = True)
    riderRating = models.CharField(null = True,max_length = 255,blank = True)
    source = JSONField(blank = True,null = True)
    sourceLocationEnglish = models.CharField(null = True,max_length = 255,blank = True)
    sourceLocationHindi = models.CharField(null = True,max_length = 255,blank = True)
    status = models.CharField(null = True,max_length = 255,blank = True)
    type = models.CharField(choices = TYPE_CHOICES,blank = True,null = True,max_length = 255)

    def __str__(self):
        return self.id


class Driver(models.Model):
    id = models.CharField(primary_key = True,max_length = 255)
    aadharDocLink = models.CharField(null = True,max_length = 255,blank = True)
    adminCreditHistory = HStoreField(blank=True)
    balanceAmmount = models.FloatField(blank=True,null = True)
    banlAccName = models.CharField(null = True,max_length = 255,blank = True)
    cashRedeemPossible = models.BooleanField(blank = True,default = False)
    dOB = models.DateField(blank = True,null = True)
    driverLevel = models.IntegerField(blank=True , null=True)
    driverName = models.CharField(null = True,max_length = 255,blank = True)
    driverPicture = models.CharField(null = True,max_length = 255,blank = True)
    driverRaiting = models.FloatField(blank=True,null = True)
    driverStatus = models.CharField(choices = DRIVER_STATUS_CHOICES,blank = True,null = True,max_length = 255)
    driverVerificationStatus = models.CharField(blank=True,null=True,max_length = 255)
    erickshawNumber = models.IntegerField(blank=True,null =True)
    fcmToken = models.CharField(blank=True,null = True,max_length = 255)
    ifscCode = models.CharField(blank=True,null = True,max_length = 255)
    lastKnownLocation = HStoreField(blank = True)
    licenseDocLink = models.CharField(blank=True,null = True,max_length = 255)
    mobile = models.CharField(blank=True,null = True,max_length = 255)
    pendingAmount = models.FloatField(blank=True,null = True)
    psvDocLink = models.CharField(blank=True,null = True,max_length = 255)
    redeemRequestHistory = HStoreField(blank=True)
    referralMoney = models.CharField(blank=True,null = True,max_length = 255)
    referralTo = HStoreField(blank=True)
    seats = HStoreField(blank=True)
    soloExpressHistory = HStoreField(blank=True)
    soloRideHistory = HStoreField(blank=True)

    def __str__(self):
        return self.id
