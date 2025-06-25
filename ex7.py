import csv

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


def get_low_stock_products(threshold):
    low_stock_products = []
    for product in inventory:
        if product['stock'] < threshold:
            low_stock_products.append(product['name'])
    return low_stock_products

result = get_low_stock_products(100)

print(f"{result}") 

csv_file_name2 = "lowstockproducts.csv"

field_names= ["id", "name", "price", "stock"]

print(f"attempt to write inventory data to {csv_file_name2}")

try:
    with open(csv_file_name2, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

#write the header row
        writer.writeheader()
        print("csv headers written")

#write rows

        writer.writerows(result)
        print(f"successfully wrote {len(result)} inventory records to {csv_file_name2}")

except IOError as e:
     print("error: could not write to {csv_file_name}. {e}")

except Exception as e:
    print("unexpected errror occured. {e}")

