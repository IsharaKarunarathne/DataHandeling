import csv

csvfilename = "employees.csv"

target_department = "hr"

print(f"attempting to read employee data from {csvfilename} and filter by {target_department}")


filtered_employees = []

try:
    with open(csvfilename, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row.get('department') == target_department:
                filtered_employees.append(row)
    print(f"\n employees in the {target_department} department")
    print(f"filtered employees list: {filtered_employees}")

   
    

except FileNotFoundError:
    print(f"file not found")

except Exception as e:
    print(f"an unexpected error occured:")

