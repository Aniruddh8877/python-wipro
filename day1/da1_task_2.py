#a fitness app recode calories cunsumed and burned.
# the goal is to calcuate the net calories  and determine if 
#the user has met their calorie deficit goal

#requeriments:
#input: calories consumed (int) and colarires bured(int)
#net_calories = consumed_calories - burned_calories
#boolean: goal_achieved = net_calorie<2000
#output: display net calores and goal status


consumed_calories = int(input("Enter calories consumed: \n"))
burned_calories = int(input("Enter calories burned: \n"))

net_calories = consumed_calories - burned_calories

goal_achieved = net_calories < 2000

print("Net Calories:", net_calories)
print("Goal Achieved:", goal_achieved)





print("----------------------------------------------------------------------------------------")
#a ride_sharing company needs a python script to calculate the total fare 
# based on distance and determine if the fare exceeds a premium ride threshold

#requeriments:
#input: distance traveled (float) and rate per km (float)
#fare = distance * rate
#boolean is_premium = fare>500
# output: display total fare and premium status

distance_traveled = float(input("Enter distance traveled (in km): \n"))
rate_per_km = float(input("Enter rate per km: \n"))

total_fare = distance_traveled * rate_per_km

is_premium = total_fare > 500

print("Total Fare:", total_fare)
print("Premium Ride:", is_premium)
