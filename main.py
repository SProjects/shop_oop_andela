from app.shop import Shop
from app.item import StockItem
from app.customer import Customer
from app.shopping_cart import ShoppingCart


def main():
    shop = Shop('Nakumatt')
    stock_shop(shop)

    cart = ShoppingCart()
    customer = Customer('Daniel Sebuuma', cart)
    customer.add_to_cart('Blueband', 5)
    customer.add_to_cart('Toothpaste', 2)
    print "Shopping Cart contains:: {}".format(cart)

    print customer.check_out(shop)


def stock_shop(shop):
    items = [StockItem('Blueband', 4000), StockItem('Toothpaste', 3000)]
    for item in items:
        shop.add_stock(item, 100)

if __name__ == '__main__':
    main()

