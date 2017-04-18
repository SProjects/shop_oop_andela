class ShoppingCart:
    def __init__(self):
        self.line_items = []

    def add_item(self, line_item):
        self.line_items.append(line_item)

    def remove_item(self, line_item):
        self.line_items.remove(line_item)

    def total_cost(self, shop):
        total = 0
        for line_item in self.line_items:
            total += shop.stock.get_sub_total(line_item)
        return total

    def __str__(self):
        result = ''
        for item in self.line_items:
            result += '| {0}: {1} pieces | '.format(item.name, item.quantity)
        return result

