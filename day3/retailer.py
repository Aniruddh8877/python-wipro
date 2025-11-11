'''
Description
A retail store keeps track of daily sales, product categories, and discounts.
Each day’s data is stored in dictionaries inside a list for easy management.

Sample Input

sales_data = [
{"day": "Monday", "sales": [1500, 2300, 1800],
"categories": {"Electronics", "Groceries"}},
{"day": "Tuesday", "sales": [2500, 1700, 2900],
"categories": {"Clothing", "Groceries"}},
{"day": "Wednesday", "sales": [3100, 2200, 3300],
"categories": {"Electronics", "Furniture"}}
]
Operations to Perform
1. Add new day data for Thursday using append().
2. Remove “Tuesday” data using pop() and store it separately.
3. Calculate total and average sales for each day using sum() and len().
4. Find all categories sold during the week using union() of sets.
5. Add a new category “Discounted” to all days using add().

Expected Output
Added new day: Thursday
Removed Tuesday data
Total & Average Sales:
Monday: 5600 (avg: 1866.67)
Wednesday: 8600 (avg: 2866.67)
Thursday: 9000 (avg: 3000.0)
All categories this week: {'Furniture', 'Discounted',
'Electronics', 'Groceries'}
Sorted days by total sales: [('Monday', 5600), ('Wednesday',
8600), ('Thursday', 9000)]

'''

sales_data = [
    {"day": "Monday", "sales": [1500, 2300, 1800], "categories": {"Electronics", "Groceries"}},
    {"day": "Tuesday", "sales": [2500, 1700, 2900], "categories": {"Clothing", "Groceries"}},
    {"day": "Wednesday", "sales": [3100, 2200, 3300], "categories": {"Electronics", "Furniture"}}
]
print("Initial sales data:", sales_data, "\n")

# 1. Add a new day data for Thursday using append().
new_day = {"day": "Thursday", "sales": [4000, 5000, 6000], "categories": {"Electronics", "Furniture"}}
sales_data.append(new_day)
print("After adding new day:", sales_data, "\n")

# 2. Remove "Tuesday" data using pop() and store it separately.
removed_day = sales_data.pop(1)
print("Removed Tuesday data:", removed_day, "\n")

# 3. Calculate total and average sales for each day using sum() and len().
for day in sales_data:
    total_sales = sum(day["sales"])
    average_sales = total_sales / len(day["sales"])
    print(f"{day['day']}: Total Sales = {total_sales}, Average Sales = {average_sales:.2f}")
print()

# 4. Find all categories sold during the week using union() of sets.
all_categories = set()
for day in sales_data:
    all_categories = all_categories.union(day["categories"])
print("All categories this week:", all_categories, "\n")

# 5. Add a new category "Discounted" to all days using add().
for day in sales_data:
    day["categories"].add("Discounted")
print("After adding 'Discounted' category to all days:", sales_data, "\n")