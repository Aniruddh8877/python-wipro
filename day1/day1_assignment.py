# # Challenge 1: Automated Financial Ticker Script

# opening_price = float(input("Enter Opening Price: "))
# closing_price = float(input("Enter Closing Price: "))
# daily_volume = int(input("Enter Daily Volume: "))

# average_price = (opening_price + closing_price) / 2
# is_high_volume = daily_volume > 500000

# print("\n--- Ticker Analysis ---")
# print("Average Trade Price:", average_price)
# print("High Volume Day Check:", is_high_volume)
# print("Total Daily Volume (as text): " + str(daily_volume))







# # Challenge 2: E-commerce Discount and Loyalty Script

# Base_Cost = 499.99
# Customer_is_Loyal = True
# Inventory_Flags = 10   # binary 1010

# Discounted_Cost = Base_Cost * 0.85    # 15% discount
# Final_Int_Cost = int(Discounted_Cost)  # truncate decimal

# is_VIP_eligible = Customer_is_Loyal and Final_Int_Cost > 400
# Stock_Alert = (Inventory_Flags & 2) != 0   # Check 2nd bit

# print("\n--- Checkout Summary ---")
# print("Initial Cost:", Base_Cost)
# print("Discounted Cost:", Discounted_Cost)
# print("Final Integer Cost:", Final_Int_Cost)
# print("VIP Eligible:", is_VIP_eligible)
# print("Stock Alert (2nd bit check):", Stock_Alert)
