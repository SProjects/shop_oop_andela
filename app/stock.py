class Stock:

    def __init__(self):
        self.stock_items = {}

    def update_stock(self, item, quantity):
        if self.stock_items.has_key(item.name):
            self.stock_items[item.name] += quantity
        else:
            self.stock_items[item.name] = quantity

