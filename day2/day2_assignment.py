print("--- Quarterly Performance Report ---")
print("ID       | SALES ($)   | PROJECTS | RATING")
print("--------------------------------------------")
report_lines = []  

while True:
    emp_id = input("Enter Employee ID (or 'DONE' to finish): ").strip()
    if emp_id.upper() == "DONE":
        break

    total_sales = float(input(f"Enter total sales for {emp_id}: "))
    projects = int(input(f"Enter number of projects for {emp_id}: "))

    if total_sales >= 150000 and projects >= 5:
        rating = "Rating A"
    elif total_sales >= 100000 or projects >= 3:
        rating = "Rating B"
    else:
        rating = "Rating C"

    report_lines.append(f"{emp_id:<8} | {total_sales:,.2f} | {projects:<8} | {rating}")
print("--------------------------------------------")
for line in report_lines:
    print(line)

print("--------------------------------------------")
print("Report Generation Complete.")








stocks_input = input("Enter comma-separated stock levels (e.g. 10, 5, 50, 2, 18): ")
stock_levels = [int(x.strip()) for x in stocks_input.split(",")]

print("\nChecking Batch...")

for stock in stock_levels:
    if stock == 0:
        print("EMERGENCY: Production Halted.")
        break
    elif stock > 40:
        print(f"Item Stock {stock}: (Skipped: Stock is sufficient.)")
        continue
    elif stock <= 5:
        print(f"Item Stock {stock}: Urgent Reorder.")
    elif stock <= 20:
        print(f"Item Stock {stock}: Standard Reorder.")
    else:
        print(f"Item Stock {stock}: Stock OK.")

print("Batch Check Complete.")
