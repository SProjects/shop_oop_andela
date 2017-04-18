import unittest
from app.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_customer_responds_to_name_property(self):
        customer = Customer('Mukasa John')
        self.assertEqual(customer.name, 'Mukasa John')