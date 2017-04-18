import unittest
from app.stock import Stock
from app.item import StockItem


class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock()

    def test_stock_adds_new_stock_items(self):
        item = StockItem('Fresh Diary Milk', 1000)
        self.stock.update_stock(item, 20)
        self.assertEqual(self.stock.stock_items, {'Fresh Diary Milk':
                                                      {'name': 'Fresh Diary Milk', 'quantity': 20, 'unit_price': 1000}})

    def test_stock_adds_multiple_stock_items(self):
        items = [StockItem('Fresh Diary Milk', 1000), StockItem('Bic Pen', 2000)]
        for item in items:
            self.stock.update_stock(item, 20)
        self.assertEqual(self.stock.stock_items, {'Fresh Diary Milk':
                                                      {'name': 'Fresh Diary Milk', 'quantity': 20, 'unit_price': 1000},
                                                  'Bic Pen':
                                                      {'name': 'Bic Pen', 'quantity': 20, 'unit_price': 2000}
                                                  })

    def test_stock_updates_existing_stock_item(self):
        item = StockItem('Fresh Diary Milk', 1000)
        self.stock.update_stock(item, 20)
        self.stock.update_stock(item, 40)
        self.assertEqual(self.stock.stock_items, {'Fresh Diary Milk':
                                                      {'name': 'Fresh Diary Milk', 'quantity': 60, 'unit_price': 1000}})
