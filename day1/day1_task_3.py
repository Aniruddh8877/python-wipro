# # you are developin a billing script for a
# #  power company
# # the program should calculate the 
# # total bill after appling a
# # usage surcharge, check for high-consumption
# # customer, and verfiy service  alert
# # flags useing bitwise operation 




# base_units = 350
# rate_per_unit = 5.75  
# service_flags = 9

# total_cost = base_units * rate_per_unit
# if base_units > 300:
#     total_cost *=1.10

# final_bill_int = int(total_cost)
# is_high_consumption = base_units > 300
# if is_high_consumption:
#     service_alert = (service_flags & 1) !=0
# else:
#     service_alert = (service_flags & 0) !=0

# print("total Bill (Integer):", total_cost)
# print ("final billl int", final_bill_int)
# print("is high user", is_high_consumption)
# print("service alert", service_alert)




Base_Salary = 60000.0
Tax_Percent = 10
Attendance_Flags = 6

Net_Salary = Base_Salary - (Base_Salary * Tax_Percent / 100)
Bonus_Salary = Net_Salary * 1.05
Final_Salary_Int = int(Bonus_Salary)

Eligible_for_Bonus = Base_Salary > 50000 and True
Perfect_Attendance = (Attendance_Flags & 2) != 0

print("Final Salary:", Final_Salary_Int)
print("Bonus Eligibility:", Eligible_for_Bonus)
print("Perfect Attendance:", Perfect_Attendance)
