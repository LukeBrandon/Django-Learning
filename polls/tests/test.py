from django.test import RequestFactory, TestCase

from rest_framework.test import APIClient
from rest_framework import status


class TestingTesting(TestCase):

    """
    This is for testing testing
    """

    @classmethod
    def setUp(cls) -> None:
        print("Starting setUp of Testing  Test")

    def test_stuff(self):
        print("Testing testing testin")
