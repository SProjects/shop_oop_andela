import unittest
from app.shop import Stock, Item


class TestStock(unittest.TestCase):

    def test_stock_adds_new_stock_items(self):
        item = Item('Fresh Diary Milk', 1000)
        stock = Stock(item, 20)
        self.assertEqual(stock.stock_items, {'Fresh Diary Milk': 20})