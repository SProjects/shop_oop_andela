class Item(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name


class LineItem(Item):
    def __init__(self, name, quantity):
        super(self.__class__, self).__init__(name)
        self.quantity = quantity


class StockItem(Item):
    def __init__(self, name, unit_price):
        super(self.__class__, self).__init__(name)
        self.unit_price = unit_price


