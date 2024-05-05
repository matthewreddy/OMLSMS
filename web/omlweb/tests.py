from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import SterilizerMethod

class QuestionModelTests(TestCase):
    def test_of_a_test(self):
        self.assertFalse(False);



        #"""was_published recently() returns False for questions whose pub_date is in the future."""
        #time = timezone.now() + datetime.timedelta(days=30)
        #future_question = Question(pub_date=time)
        #self.assertIs(future_question.was_published_recently(), True)