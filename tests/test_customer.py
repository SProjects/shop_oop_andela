import unittest
from app.shop import Shop
from app.customer import Customer
from app.shopping_cart import ShoppingCart
from app.item import StockItem
from app.item import LineItem


class TestCustomer(unittest.TestCase):
    def setUp(self):
        shop = Shop('Nakumatt')
        shop.add_stock(StockItem('Blueband', 4000), 100)

        cart = ShoppingCart()
        self.customer = Customer('Mukasa John', cart)

    def test_customer_responds_to_its_properties(self):
        self.assertEqual(self.customer.name, 'Mukasa John')

    def test_customer_add_item_to_cart(self):
        self.customer.add_to_cart('Blueband', 3)
        self.assertEqual(self.customer.cart.line_items, [LineItem('Blueband', 3)])


