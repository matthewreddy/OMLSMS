"""Module for defining the behavior of the updated database.
Outlining rules on how the data is expected to be stored and retrieved
in accordance with the other dialog boxes being rendered."""

import sys, datetime

from constants import *

sys.path.append(OMLWEB_PATH)
from omlweb.models import Update, Renewal, Sterilizer, Dentist
from django.db.models import F

import bulkops

def updateDatabase():
    #updates = Update.objects.all().order_by('-update_date')
    updateLateFees()
    #if not updates or updates[0].update_date != datetime.date.today():
    #    updateLateFees()
    #    update = Update(update_date = datetime.date.today())
    #    update.save()

def updateLateFees():
    # Gets todays date
    today = datetime.date.today()
    # date is two years in the past from today
    date = datetime.datetime.combine(today, datetime.datetime.min.time()) - datetime.timedelta(days=MAX_DAYS_FOR_COLLECTIONS)
    # Gets list of renewals that are greater than 2 years ago today
    list = Renewal.objects.filter(renewal_date__gte=date)
    list = list.exclude(payment_amount__gte=F('renewal_fee')) #if they pay the principal, don't add to late fees
    list = list.exclude(renewal_fee=0)
    # Not sure about all of this
    #list = list.exclude(late_fee=MAX_LATE_FEE)
    
    #list = list.filter(inactive_date__isnull=True)
    #list = list.filter(sterilizer__inactive_date__isnull=True)
    #list = list.filter(sterilizer__dentist__inactive_date__isnull=True)
    
    updated = []
    for renewal in list:
        lateFee = calculateLateFee(renewal)
        if lateFee != renewal.late_fee:
            renewal.late_fee = lateFee
            updated.append(renewal)
    if updated:
        bulkops.update_many(updated, ["late_fee"]) #update all lateFees in one query

#
# How to calculate late fees
#
# no charge until 90 days. $20 fee after that
# if still overdue after another 90 days, add $20
# Reflected by #7 on word document
# No late fee to exceed MAX_LATE_FEE (to prevent accidental excessive bills)
#
def calculateLateFee(Renewal: Renewal):
    if Renewal.renewal_fee == 0:
        return 0
    
    daysOverdue = (datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time()) - Renewal.renewal_date).days
    # Changed to 90 to reflect Dr.Reisdorf's request
    if daysOverdue < 90:
        return 0
    else:
        # Integer division so we get an integer back
        # Aka, 91 // 90 = 1, 1*20 = 20
        # MAX_LATE_FEE set to 100
        return min((daysOverdue//90) * 20, MAX_LATE_FEE)