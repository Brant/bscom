"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "bscom/tests/runtests.py".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase


class SanityCheckTestCase(TestCase):
    """
    Test case to check sanity of test suite
    """
    def test_addition(self):
        """
        Does 1 + 1 still equal 2?
        """
        self.assertEquals(1+1, 2)