#inventory using lst of dictionaries

inventory = [
{"id": "p001", "name": "laptop", "price": 1200, "stock": 50},
{"id": "p002", "name": "mouse", "price": 200, "stock": 70},
{"id": "p003", "name": "keyboard", "price": 500, "stock": 10},
{"id": "p004", "name": "monitor", "price": 1500, "stock": 20},
{"id": "p005", "name": "webcam", "price": 400, "stock": 5}
]

print("initial inventory")

for product in inventory:
    print(f"ID:{product['id']}, name: {product['name']}, price: {product['price']}, stock: {product['stock']}\n")


def update_stock(product_id, quantity):
    found = False
    for product in inventory:
        if product['id'] == product_id:
            if product['stock'] + quantity >= 0:
                product['stock']= product['stock'] + quantity
                print(f"updated stock for {product['name']} (ID:{product['id']}). cannot reduce stock by {abs(quantity)}.")
            else:
                print(f"NOT ENOUGH stock for {product['name']}")
            found = True
            break
    if not found:
        print(f"error product with id {product['name']} (ID:{product['id']}) not found in the stock")


def get_low_stock_products(threshold):
    low_stock_products = []
    for product in inventory:
        if product['stock'] < threshold:
            low_stock_products.append(product['name'])
    return low_stock_products


print("demonstrating stock updates")
x = input("enter the id: ")
y = input("enter the arrived quantity: ")
update_stock(x, y)
print(f"new stock size of: {x} is {product['stock']}")

            

