from Implementation.ProductsImplementation import ProductsImplementation
from Implementation.VendorImplementation import VendorImplementation
from Models.VendorSessionModel import VendorSessionModel

if __name__ == '__main__':

    vendor = VendorImplementation()
    username="Rossum"
    password="rossum_pw"
    login_res = vendor.login(username,password)
    if login_res == False:
        print("Invalid Username or password")
    else:
        print("User "+username+" logged in successfully!")
        products = ProductsImplementation(username)
        products.add_product("Lenovo Thinkpad", "Laptop", 40, 20000)
        products.add_product("Dell Inspiron", "Laptop", 40, 30000)
        products.add_product("Acer razor", "Laptop", 40, 25000)
        products.add_product("Asus Tinker", "Laptop", 40, 20000)
        products.add_product("Lenovo Gaming", "Laptop", 40, 20000)

        product_to_find="Lenovo Gaming"
        search_product = products.search_product_by_name(product_to_find)
        print("searching "+product_to_find+"...")
        if (search_product):
            print(search_product)
        else:
            print("No product exists by the name "+product_to_find)
        
        all_products = products.get_all_products()
        print("All product  are :-")
        if (all_products):
            print(all_products)
        else:
            print("No product is available to fetch.")
            
        vendor.logout(username)