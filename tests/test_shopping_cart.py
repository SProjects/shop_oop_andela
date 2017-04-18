import unittest
from app.shopping_cart import ShoppingCart
from app.item import LineItem


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_shopping_cart_adds_line_items(self):
        line_item = LineItem('Blueband', 3)
        self.cart.add_item(line_item)
        self.assertEqual(self.cart.line_items, [line_item])

    def test_shopping_cart_removes_items(self):
        line_item_to_remove = LineItem('Blueband', 3)
        line_items = [LineItem('Toothpaste', 5), line_item_to_remove]
        for line_item in line_items:
            self.cart.add_item(line_item)
        self.cart.remove_item(line_item_to_remove)
        self.assertTrue(self.cart.line_items[0] == LineItem('Toothpaste', 5))


