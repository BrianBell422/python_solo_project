import unittest
from models.bike import Bike

class TestBike(unittest.TestCase):

    def setUp(self):
        self.bike = Bike()

    def test_has_name(self):
        self.assertEqual()