import unittest
from app.shop import Item


class TestItem(unittest.TestCase):

    def test_item_responds_to_properties(self):
        item = Item('Bic Pen', 2000)
        self.assertEqual([item.name, item.unit_price], ['Bic Pen', 2000])

