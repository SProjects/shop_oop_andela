from stock import Stock


class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.line_items = []

    def add_item(self, line_item):
        self.line_items.append(line_item)

    def remove_item(self, line_item):
        self.line_items.remove(line_item)

    def check_out(self):
        return "{0} has paid UGX: {1}".format(self.customer, self._total_cost())

    def _total_cost(self):
        total = 0
        for line_item in self.line_items:
            total += Stock().get_sub_total(line_item)
        return total

