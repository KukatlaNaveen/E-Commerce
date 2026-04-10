from storage import Storage

class Dealer:
    def __init__(self,name,filename):
         self.name=name
         self.store=Storage(filename)
    def get_product(self):
        data=self.store.load()
        if not isinstance(data,list):
            return []
        return data
    def update_product(self,name,price,quantity):
       data=self.get_product()
       
       for p in data:
          if p["name"].lower()==name.lower():
             if p["quantity"]>quantity:
                print("stock is enough")
                return
             else:
                p["quantity"]+=quantity
                self.store.save(data)
                print("stock updated")
                return
       data.append({
            "name":name,
            "price":price,
            "quantity":quantity
       })
       self.store.save(data)
       print("producted added")
    def view_product(self):
      data=self.get_product()
      if not data:
         print("No products")
         
      for p in data:
         print(p["name"],p["price"],p["quantity"])