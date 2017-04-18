import unittest
from app.item import LineItem


class TestStockItem(unittest.TestCase):

    def test_item_responds_to_properties(self):
        item = LineItem('Bic Pen', 20)
        self.assertEqual([item.name, item.quantity], ['Bic Pen', 20])

