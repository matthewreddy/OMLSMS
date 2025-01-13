import sys
import os

# Add the parent directory of db_rewrite to sys.path, 
# important so that the methods can be found to test
# Still in progress but leaving for now
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from django.test import TestCase
from omlweb.models import Lot, Renewal, Sterilizer, Dentist, Test, State
from db_rewrite.reportdlg import getDentistNames, RenewalToDentistID, SterilizerToDentistID

class ReportDlgTestCase(TestCase):

    def setUp(self):
        nc = State.objects.create(
                                   abbreviation="NC", 
                                   name="North Carolina"
                               )
        Dentist.objects.create(practice_name = "Grayson Family Practice",
                               lname = "Clark",
                               fname = "Grayson",
                               title = "Dr.",
                               contact_lname = "Clark",
                               contact_fname = "Grayson",
                               contact_title = "Dr.",
                               address1= "1020 Cambridge Ct",
                               city="Lenoir",
                               state= nc,
                               zip="28645",
                               phone = "8287290328",
                               )
    
    def test_get_dentist_names(self):
        """Tests the get dentist names method in ReportDlg"""
        dentist = Dentist.objects.get(practice_name="Grayson Family Practice")
        itemList = [dentist]
        list = getDentistNames(itemList, True)
        print(list)


