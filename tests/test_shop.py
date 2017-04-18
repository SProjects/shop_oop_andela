import unittest
from app.shop import Shop


class TestShop(unittest.TestCase):

    def setUp(self):
        self.shop = Shop('Nakumatt')

    def test_shop_responds_to_name_property(self):
        self.assertEqual(self.shop.name, 'Nakumatt')