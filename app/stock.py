class Stock(object):

    def __init__(self):
        self.stock_items = {}

    def update_stock(self, item, quantity):
        if self.stock_items.has_key(item.name):
            self.stock_items[item.name]['quantity'] += quantity
        else:
            self.stock_items[item.name] = {'name': item.name, 'unit_price': item.unit_price, 'quantity': quantity}

    def get_sub_total(self, item):
        item_unit_price = self.stock_items[item.name]['unit_price']
        return item.quantity * item_unit_price
