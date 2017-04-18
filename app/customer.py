class Customer:
    def __init__(self, name):
        self.name = name

    def check_out(self, cart):
        return "{0} has paid UGX: {1}".format(self.name, cart.total_cost())


