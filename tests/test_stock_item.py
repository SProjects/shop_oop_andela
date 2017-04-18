import unittest
from app.item import StockItem


class TestStockItem(unittest.TestCase):

    def test_item_responds_to_properties(self):
        item = StockItem('Bic Pen', 2000)
        self.assertEqual([item.name, item.unit_price], ['Bic Pen', 2000])

