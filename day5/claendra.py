#display the month calendar

import calendar

# print(calendar.month(2025,11))

#check leap year or not

# print(calendar.isleap(2024))

# def is_leap(year):
#      if (year%4 ==0 and year%100!=0) or (year%400==0):
#           return True
#      else:
#           return False
     
# year = int(input("enter a year to check wheather is a leap year or not "))

# if is_leap(year):
#      print(f'{year} is a leap year')

# else:
#      print(f'{year} is not a leap year')

#count leap year in a range

# print(calendar.leapdays(2000,2025))

#display all leap year between ranage

# start =2000
# end =2025
# for year in range(start,end):
#      if(calendar.isleap(year)):
#           print(year,end=' ')


#print week days
# print(calendar.weekday(2025,11,12))
# day= calendar.weekday(2025,11,12)
# print(calendar.day_name[day])