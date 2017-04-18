from item import LineItem


class Customer:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def check_out(self, shop):
        return "{0} has paid UGX: {1}".format(self.name, self.cart.total_cost(shop))

    def add_to_cart(self, item_name, quantity):
        line_item = LineItem(item_name, quantity)
        self.cart.add_item(line_item)
        return self.cart


