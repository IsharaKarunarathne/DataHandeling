import json
import datetime

product_data = {
    "products": [
        {"id": "A1", "name": "keyboard", "price": 75.00, "AVAILABLE": True},
        {"id": "A2", "name": "mouse", "price": 25.50, "AVAILABLE": False},
        {"id": "A3", "name": "monitor", "price": 300.00, "AVAILABLE": True},
        {"id": "A4", "name": "webcam", "price": 50.00, "AVAILABLE": True},
        {"id": "A5", "name": "headphones", "price": 120.00, "AVAILABLE": False}
],
"LAST UPDATED": datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S")

}


json_file_name = "products.json"

print(f"attempting to write product data to '({json_file_name})'")

try:
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(product_data,json_file, indent=4)
        print(f"succesfully write to {json_file_name}")

except IOError as e:
    print(f"error: could not write to file '{json_file_name}'. {e}")
except Exception as e:
    print(f"error:an unexpected error occured: {e}")
print(f"\n please check the {json_file_name} file manually in a text editor to verify")

