class Shop(object):
    def __init__(self, name):
        self.name = name


class Stock:
    stock_items = {}

    def __init__(self, item, quantity):
        self._update_stock(item, quantity)

    def _update_stock(self, item, quantity):
        self.stock_items[item.name] = quantity


class Item:
    def __init__(self, name, unit_price):
        self.name = name
        self.unit_price = unit_price


