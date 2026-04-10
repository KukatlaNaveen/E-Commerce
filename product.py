class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart(Product):  # inheritance
    def __init__(self):
        self.__items = []   # encapsulation

    def add_product(self, product):
        self.__items.append(product)
        print(product.name, "added to cart")

    def remove_product(self, name):
        for item in self.__items:
            if item.name == name:
                self.__items.remove(item)
                print(name, "removed from cart")
                return
        print("Product not found")

    def show_products(self):
        if not self.__items:
            print("Cart empty")
            return
        for item in self.__items:
            print(item.name, item.price)

    def total_price(self):
        total = sum(item.price for item in self.__items)
        print("Total price:", total)
        
        if total>1000:
            discount=total*0.10
            total-=discount
            print("Total price with discount:",total)
        else:
            print("discount is not available")

    def get_items(self):
        return self.__items