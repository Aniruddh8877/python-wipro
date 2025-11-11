import datetime as dt

# print(dt.datetime.now())
# print(dt.datetime.now().year)
# print(dt.datetime.now().month)
# print(dt.datetime.now().day)
# print(dt.datetime.now().hour)
# print(dt.datetime.now().minute)
# print(dt.datetime.now().second)
# print(dt.datetime.now().microsecond)


#formate dates

print(dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S"))
print(dt.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"))
print(dt.datetime.now().strftime("%A, %B %d, %Y"))
print(dt.datetime.now().strftime("%a, %b %d, %Y"))
print(dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))



'''
%a: abbreviated weekday name
%A: full weekday name
%w: weekday as a decimal number
%b: abbreviated month name
%B: full month name
%m: month as a decimal number
%d: day of the month as a decimal number
%H: hour (24-hour clock) as a decimal number
%I: hour (12-hour clock) as a decimal number
%M: minute as a decimal number
%S: second as a decimal number
%p: AM or PM
'''