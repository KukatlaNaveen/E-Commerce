from user import User
from storage import Storage
# method overriding
class Admin(User):
    def __init__(self):
        super().__init__()
        self.product_store = Storage("products.json")

    # only one admin allowed
    def register(self, username, password):
        if len(self._User__users) >= 1:
            print("Admin already exists")
            return False
        return super().register(username, password)

    def add_product(self, name, price,quantity):
        data = self.product_store.load()
        if not isinstance(data, list):
            data = []

        data.append({"name": name, "price": price,"quantity":quantity})
        self.product_store.save(data)
        print("Product added")

    def remove_product(self, name):
        data = self.product_store.load()
        new_data = [p for p in data if p["name"] != name]
        
        if len(data)==len(new_data):
            print("product not found")
        else:
            self.product_store.save(new_data)
            print("Product removed")

    def view_products(self):
        data = self.product_store.load()
        print(data)
        if not data:
            print("No products")
            return

        for p in data:
            print(p["name"], p["price"],p["quantity"])
        
    def add_stock(self,name,quantity):
        data=self.product_store.load()
        
        for p in data:
            if p["name"]==name:
                p["quantity"]+=quantity
                self.product_store.save(data)
                print("stock added successfully")
                return
            print("product  not found")