import csv

employee_data = [
    {"name": "Alis Smith", "department": "hr", "salary": 60000},
    {"name": "John Davis", "department": "finance", "salary": 72000},
    {"name": "Priya Kaur", "department": "engineering", "salary": 95000},
    {"name": "Liam Chen", "department": "marketing", "salary": 67000},
    {"name": "Sara Lopez", "department": "hr", "salary": 62000}

]

csv_file_name = "employees.csv"

field_names= ["name", "department", "salary"]

print(f"attempt to write employee data to {csv_file_name}")

try:
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

#write the header row
        writer.writeheader()
        print("csv headers written")

#write rows

        writer.writerows(employee_data)
        print(f"successfully wrote {len(employee_data)} employee records to {csv_file_name}")

except IOError as e:
     print("error: could not write to {csv_file_name}. {e}")

except Exception as e:
    print("unexpected errror occured. {e}")


