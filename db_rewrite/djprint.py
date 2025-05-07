"""Several helper functions used around the application to get corresponding data."""

import sys
from datetime import date, timedelta
from constants import *

sys.path.append(OMLWEB_PATH)
from django.template import Context
from django.template.loader import get_template, render_to_string
from omlweb.views import getBillingData
from omlweb.models import Dentist, Renewal, Sterilizer, Test


def getBillForSterilizer(sterilizer_id, dentist=None, renewal=None):
    """Calculates a bill for a specific sterilizer by its ID."""
    if not dentist:
        dentist_id = int(str(sterilizer_id).zfill(STERILIZER_ID_WIDTH )[0:DENTIST_ID_WIDTH])
        dentist = Dentist.objects.get(id=dentist_id)
    t = get_template('bill.html')
    payment = getBillingData(sterilizer_id)

    # want to show unpaid balances plus last paid balance
    # show at least the last three balances if possible
    i = 1
    while i < len(payment['balances']) and payment['balances'][-i]['amount'] != 0:
        i = i + 1

    payment['renewals'] = payment['renewals'][:]
    value = min(len(payment['renewals']), max(i, 3))
    payment['renewals'] = payment['renewals'][-value:]

    if renewal:
        payment['renewals'].append(renewal)
        amount = ZeroNone(renewal.renewal_fee) + ZeroNone(renewal.late_fee) - \
                 ZeroNone(renewal.payment_amount)
        dict = {
        'renewal_id' : renewal.id,
        'amount' : amount,
        }
        payment['balances'].append(dict)
        payment['amount'] = payment['amount'] + amount
        payment['due_date'] = renewal.renewal_date + datetime.timedelta(days=30)

    return render_to_string('bill.html', {
        'dentist': dentist,
        'payment': payment
    })
    

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def encodeTo128Font(value):
    if value == 0:
        return 128
    elif value >= 95:
        return value + 50
    else:
        return value + 32

def encodeToCode128(id):
    """Encode ID string to condensed Code 128c
    (Start C) (Encoded Pairs) (Checksum) (End Char)
    checksum =  Value of Start C + (Value * Position) of Encoded Pairs
    """
    checksum = 105
    code = ""
    for position, pair in enumerate(chunker(id, 2)):
        checksum += int(pair) * (position + 1)
        code = code + "&#%d" % encodeTo128Font(int(pair))
    checksum = encodeTo128Font(checksum % 103)
    return "&#155" + code + ("&#%d" % checksum) + "&#156"

def getRenewalLabelsForSterilizers(sterilizers, dentists, lot):
    """Return renewal labels based on given sterilizers, dentists, and lot."""
    renewal_ids = []
    barcodes = []
    numLabels = 0
    for sterilizer in sterilizers:
        numLabels += sterilizer.num_tests
        base = ("%d%d" % (sterilizer.id, lot.id)).zfill(RENEWAL_ID_WIDTH)
        ids = []
        codes = []
        for strip in range(1, sterilizer.num_tests + 1):
            id = "%s%s" % (base, str(strip).zfill(STRIP_ID_WIDTH))
            ids.append(id)
            codes.append(encodeToCode128(id))
        renewal_ids.append(ids)
        barcodes.append(codes)

    z = zip(sterilizers,renewal_ids,barcodes)

    return render_to_string('renewallabel.html', {
        'today': date.today(),
         'sterilizers': sterilizers,
        'dentists': dentists,
        'lot': lot,
        'zips': z,
        'image_directory': IMAGES_PATH,
        'num_labels': numLabels,
    })
    
def getBillsForDentist(dentist):
    """Return bills for a specific dentist."""
    (start, stop) = GetSterilizerIDRange(dentist.id)
    sterilizers = Sterilizer.objects.filter(id__range=(start, stop))\
                     .filter(inactive_date=None)
    if not sterilizers:
        return ""
    html = ""
    for i,sterilizer in enumerate(sterilizers):
        if i != len(sterilizers) - 1:
            html += getBillForSterilizer(sterilizer.id, dentist) + \
            "\r\n" + "<pdf:nextpage />" + "\r\n"
        else:
            html += getBillForSterilizer(sterilizer.id, dentist) 
    return(html)

def getResultsDateRange(sterilizer):
    """Calculate date range using the datetime library for a sterilizer."""
    r = Renewal.objects.filter(sterilizer__id=sterilizer.id)
    r = r.filter(inactive_date__isnull=True).order_by("-renewal_date")
    if len(r) > 1:
        # For sterilizer with multiple renewals, include history from shortly
        # before previous renewal until today
        start_date = r[1].renewal_date - timedelta(days=REPORT_HISTORY_EXTRA_DAYS)
    elif r:
        # For sterilizer with only one renewal, report whole history
        start_date = r[0].renewal_date
    else:
        # Report for sterilizer with no renewals (this really should not be done)
        start_date = date.today() - timedelta(days=REPORT_HISTORY_DEFAULT_DAYS)
    return (start_date, date.today())
  
def getResultsLetter(dentist, sterilizers, date_range):
    """Generate a letter displaying results for a dentist. Also requires sterilizers and a date range."""
    results_list = []
    for sterilizer in sterilizers:
        if not date_range:
            (start_date, stop_date) = getResultsDateRange(sterilizer)
        else:
            (start_date, stop_date) = date_range
        q = Test.objects.filter(renewal_id__sterilizer_id=sterilizer.id)
        q = q.filter(start_date__range=(start_date, stop_date))
        q = q.order_by('sample_date')
        dict = {
            'tests': q,
            'sterilizer': sterilizer,
            'start_date': start_date,
            'stop_date': stop_date,
        }
        results_list.append(dict)

    return render_to_string('report.html', {
        'today': date.today(),
        'dentist': dentist,
        'result_summaries': results_list,
        'image_directory': IMAGES_PATH,
    })
    
def getReportForSterilizer(sterilizer_id, date_range = None):
    """Generates and returns a report for a specific sterilizer by its ID."""
    dentist_id = str(sterilizer_id).zfill(STERILIZER_ID_WIDTH)[0:DENTIST_ID_WIDTH]
    dentist = Dentist.objects.get(id=dentist_id)
    sterilizer = Sterilizer.objects.get(id=sterilizer_id)
    sterilizers = [sterilizer]
    return getResultsLetter(dentist, sterilizers, date_range)

def getReportForDentist(dentist_id, date_range = None):
    """Generates and returns a report for a specific dentist by their ID."""
    dentist = Dentist.objects.get(id=dentist_id)
    sterilizers = Sterilizer.objects.filter(dentist__id=dentist_id)
    sterilizers = sterilizers.filter(inactive_date__isnull=True)
    if not sterilizers:
        return ""
    return getResultsLetter(dentist, sterilizers, date_range)

def printNotifyLetter(dentist, test, user, contacted):
    """Helper function to render a notify letter."""
    user_override = {
        'name_title': '',
        'first_name': '',
        'last_name': '',
        'title': '',
        'signature_file': '',
    }

    return render_to_string('notify_letter.html', {
        'today': date.today(),
        'dentist': dentist,
        'test': test,
        'user': user_override,
        'contacted': contacted,
        'image_directory': IMAGES_PATH,
    })


def printDentistLabelSheet(dentists, skip):
    """Helper function to render a dentist label sheet."""
    return render_to_string('dentist_labelsheet.html', {
        'dentists': dentists,
        'skip': skip,
    })
    
def printSterilizerLabelSheet(sterilizers, dentists, skip):
    """Helper function to render a sterilizer label sheet."""
    return render_to_string('sterilizer_labelsheet.html', {
        'sterilizers': sterilizers,
        'dentists': dentists,
        'skip': skip,
    })

def testCountReport(title, testList):
    """Helper function to render testing lists."""
    return render_to_string('testcount.txt', {
        'title': title,
        'tests': testList
    })

def inactivityReport(sterilizerList, names, weeks, activity):
    """Helper function to render an inactivity report."""
    return render_to_string('inactivityreport.txt', {
        'sterilizers': sterilizerList,
        'names': names,
        'activity': activity,
        'weeks': weeks,
    })

def getAnomalyReport(suspended, s_names, overlooked, o_names):
    """Helper function to render an anomaly report."""
    return render_to_string('anomalyreport.txt', {
        'suspended': suspended,
        's_names': s_names,
        'overlooked': overlooked,
        'o_names': o_names,
    })

def printOverdueAccountList(renewalList, namesList):
    """Helper function to render an overdue report/account list."""
    return render_to_string('overduereport.txt', {
        'renewals': renewalList,
        'names': namesList,
    })

def printDailyPaymentReport(renewalList, namesList):
    """Helper function to stringify a payment report."""
    return render_to_string('paymentreport.txt', {
        'renewals': renewalList,
        'names': namesList
    })

def printQuarterlyPaymentSummary(values):
    """Helper function to render an accounts summary.
    All values must be passed directly to the function in JSON.
    """
    # Leaving this here for future developers:
    # It's unclear how to replace this function like the others, if this functionality doesn't work as intend, 
    # it will be needed to be looked into

    # Old:
    # t = get_template('accountssummary.txt')
    # c = Context(values)  # could possibly be refactored similar to the other functions
    
    # New
    return render_to_string('accountssummary.txt', values)

def viewRenewals(renewalList, namesList, header, start, stop):
    """Helper function to render renewals."""
    return render_to_string('renewallist.txt', {
        'renewals': renewalList,
        'names': namesList,
        'header': header,
        'begin_date': start,
        'end_date': stop,
    })

def viewTests(testList, header, start, stop):
    """Helper function to render tests."""
    return render_to_string('testcount.txt', {
        'tests': testList,
        'title': header,
        'begin_date': start,
        'end_date': stop,
    })

def printYearlyComplianceLetter(dentist, sterilizer, compliance, year, numTests, user):
    """Helper function to render compliance letter."""
    user_override = {
        'name_title': 'Dr.',
        'first_name': 'Apoena',
        'last_name': 'de Aguiar Ribeiro, DDS, MSc, PhD',
        'title': 'Director',
        'signature_file': 'AAR_sig.bmp',
    }

    return render_to_string('complianceletter.html', {
        'today': date.today(),
        'dentist': dentist,
        'sterilizer': sterilizer,
        'number_of_tests': numTests,
        'user': user_override,
        'report_year': year,
        'compliance': compliance,
        'image_directory': IMAGES_PATH,
    })

def printLotRecall(renewalList, namesList):
    """Helper function to render a lot recall."""
    return render_to_string('lotrecall.txt', {
        'renewals': renewalList,
        'names': namesList,
    })


def printRenewalsStarted(sterilizerList, namesList):
    """Helper function to render a renewal being started."""
    return render_to_string('startrenewal.txt', {
        'sterilizers': sterilizerList,
        'names': namesList,
    })