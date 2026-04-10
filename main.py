from user import User
from product import Product, Cart
from storage import Storage
from admin import Admin
from dealer import Dealer

def find_product(name):
    for file in["accessories.json","clothes.json"]:
        store=Storage(file)
        data=store.load()
        
        for p in data:
            if p["name"].lower()==name.lower() and p["quantity"]>0:
                return p,file
    return None,None
            
        

user_system = User()
cart = Cart()
product_store = Storage("products.json")
cart_store=Storage("cart.json")
admin=Admin()
accessories_dealer=Dealer("Accessories","accessories.json")
clothes_dealer=Dealer("Clothes","clothes.json")
while True:
    role=input("Enter role admin/user/dealer/exit:").lower()
    if role =="user":
            while True:
                print("\n1 Register")
                print("2 Login")
                print("3 Exit")

                choice= input("Enter choice: ")

                if choice == "1":
                    u = input("Username: ")
                    p = input("Password: ")
                    user_system.register(u, p)

                elif choice == "2":
                    u = input("Username: ")
                    p = input("Password: ")

                    if user_system.login(u, p):

                     while True:
                        print("\n1 Add product")
                        print("2 Remove product")
                        print("3 Show products")
                        print("4 Total price")
                        print("5 Logout")

                        c = input("Choice: ")

                        if c == "1":
                            name = input("Product name: ")
                            price = float(input("Price: "))
                            product_data,file=find_product(name)
                            
                            if product_data:
                                product=Product(product_data["name"],product_data["price"])
                                cart.add_product(product)
                                
                                #reduce stock
                                store=Storage(file)
                                data=store.load()
                                
                                for p in data:
                                    if p["name"].lower()==name.lower():
                                        p["quantity"]-=1
                                        break
                                store.save(data)
                            else:
                                print("product not available")
                                    
                            # product = Product(name, price)
                            # cart.add_product(product)

                            data = [{"name": i.name, "price": i.price} for i in cart.get_items()]
                            cart_store.save(data)

                        elif c == "2":
                            name = input("Product name: ")
                            cart.remove_product(name)

                            data = [{"name": i.name, "price": i.price} for i in cart.get_items()]
                            cart_store.save(data)

                        elif c == "3":
                            cart.show_products()

                        elif c == "4":
                            cart.total_price()

                        elif c=='5':
                            break

                elif choice == "3":
                    break
    elif role=="admin":
            while True:
                print("""
                    1.Admin Register
                    2.Login 
                    3.Back
                    """)
                c=input("Enter choice:")
                if c=='1':
                    u=input("admin name:")
                    p=input("password:")
                    admin.register(u,p)
                elif c=='2':
                    if admin.login(u,p):
                        while True:
                            print("""
                                1. Add products
                                2. Remove product
                                3. View products
                                4. add stock
                                5. Logout"""
                                )
                            c1=input("choice:")
                            if c1=='1':
                                name=input("product name:")
                                price=float(input("price:"))
                                quantity=input("quantity:")
                                admin.add_product(name,price,quantity)
                            elif c1=='2':
                                name=input("product name:")
                                admin.remove_product(name)
                            elif c1=='3':
                                admin.view_products()
                            elif c1=='4':
                                name=input("product name:")
                                quantity=int(input("Enter quantity to add: "))
                                admin.add_stock(name,quantity)
                            elif c1=='5':
                                break
                            else:
                                print("Invalid input")
                elif c=='3':
                    break
    elif role=="dealer":
        print("""
                 1.Accessories dealer
                 2.clothes dealer""")
        d_choice=input("select dealer:")
        
        if d_choice=='1':
            dealer=accessories_dealer
        elif d_choice=='2':
            dealer=clothes_dealer
        else:
            print("Invalid")
            continue
        while True:
            print("""
                  1.update product
                  2.view products""")
            c=input("choice:")
            if c=='1':
                name=input("product name:")
                price=float(input("price:"))
                quantity=int(input("quantity:"))
                dealer.update_product(name,price,quantity)
            elif c=='2':
                dealer.view_product()
            elif c=='3':
                break
            
                                