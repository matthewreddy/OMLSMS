"""Defining filters in the data that can be understood by Django."""

from django import template
import locale
import datetime

STERILIZER_ID_DIGITS = 7
RENEWAL_ID_DIGITS = 10
TEST_ID_DIGITS = 12

#locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )
locale.setlocale( locale.LC_ALL, '' )

register = template.Library()

@register.filter(name='zfill')
def zfill_filter(value, num_digits):
    """Pad a string (that holds a number) with the given number of zeroes."""
    try:
        s = str(value).zfill(num_digits)
    except:
        s = 'Err'
    return s

@register.filter(name='currency')
def currency_filter(i):
    """Filter and translate a number into currency based on locale."""
    try:
        s = locale.currency(float(i), grouping=True)
    except:
        s = 'Err'
    return s

@register.filter(name='payment')
def payment(value):
    """Format a given value into a payment."""
    try:
        s = "{:7.2f}".format(value)
    except:
        s = 'Err'
    return s

@register.filter(name='renewal_id')
def renewal_id_filter(i):
    """Format a number into a renewal ID."""
    try:
        s = str(i).zfill(RENEWAL_ID_DIGITS)
        s = s[0:STERILIZER_ID_DIGITS] + "-" + s[STERILIZER_ID_DIGITS:]
    except:
        s = 'Err'
    return s

@register.filter(name='test_result')
def test_result(i):
    """Format a number into a test result."""
    if i:
        return i
    else:
        return ""

@register.filter(name='test_id')
def renewal_id_filter(i):  # should this be called test_id_filter?
    """Format a number into a test ID."""
    try:
        s = str(i).zfill(TEST_ID_DIGITS)
        s = s[0:STERILIZER_ID_DIGITS] + "-" \
            + s[STERILIZER_ID_DIGITS:RENEWAL_ID_DIGITS] + "-" + \
            s[RENEWAL_ID_DIGITS:]
    except:
        s = 'Err'
    return s

@register.filter(name='days_overdue')
def days_overdue_filter(d):
    """Format a date into the amount of days it is past overdue."""
    try:
        s = str((datetime.date.today() - d).days)
    except:
        s = 'Err'
    return s

@register.filter(name='zip')
def zip_lists(a, b):
    """Define zipping behavior between two parameters."""
    return zip(a, b)

@register.filter(name='zip2')
def zip_lists2(a, b):
    """Define alternate zipping behavior between two parameters based on the values within the parameters."""
    return zip(zip(*a)[0], zip(*a)[1], b)

@register.filter(name='times') 
def times(number):
    """Determine the range (all numbers from 0 up to the given number) of a number."""
    return range(number)

@register.filter(name='my_add')
def my_add(a,b):
    """Define adding behavior between two parameters."""
    try:
        return (a if a else 0) + (b if b else 0)
    except:
        return 'Err'

@register.filter(name='multiply')
def multiply(a,b):
    """Define multiplying behavior between two parameters."""
    try:
        return a * b
    except:
        return 'Err'

@register.filter(name='next_label') 
def next_label(number, skip):
    """Set the cutoff for going to the next label."""
    if (number + skip) % 30 == 0:
        return "<pdf:nextpage />"
    else:
        return "<pdf:nextframe />"
    
@register.filter(name='next_frame')
def next_frame(number, num_per_page):
    """Set the cutoff for going to the next page or frame."""
    if number % num_per_page == 0:
        return "<pdf:nextpage />"
    else:
        return "<pdf:nextframe />"
