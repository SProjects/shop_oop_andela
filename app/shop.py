from app.stock import Stock


class Shop(object):
    def __init__(self, name):
        self.name = name
        self.stock = Stock()

    def add_stock(self, item, quantity):
        self.stock.update_stock(item, quantity)



