import unittest
from app.stock import Stock
from app.item import Item


class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock()

    def test_stock_adds_new_stock_items(self):
        item = Item('Fresh Diary Milk', 1000)
        self.stock.update_stock(item, 20)
        self.assertEqual(self.stock.stock_items, {'Fresh Diary Milk': 20})

    def test_stock_adds_multiple_stock_items(self):
        items = [Item('Fresh Diary Milk', 1000), Item('Bic Pen', 40)]
        for item in items:
            self.stock.update_stock(item, 20)
        self.assertEqual(self.stock.stock_items, {'Fresh Diary Milk': 20, 'Bic Pen': 20})

    def test_stock_updates_existing_stock_item(self):
        item = Item('Fresh Diary Milk', 1000)
        self.stock.update_stock(item, 20)
        self.stock.update_stock(item, 40)
        self.assertEqual(self.stock.stock_items, {'Fresh Diary Milk': 60})
