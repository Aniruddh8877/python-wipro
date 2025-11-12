import csv

# with open('test.csv', 'w', newline='') as file:   # ✅ always include newline='' on Windows
#     writer = csv.writer(file)
#     writer.writerow(['A', 'B', 'C'])
#     writer.writerow(['1', '2', '3'])
#     writer.writerow(['4', '5', '6'])
# print("CSV file created successfully.")


with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)