import re
phone= '+91-6234567890'

#\d+ = one or more digit
#\s+ = one or more space

pattern = r'^\+91-[6-9]\d{9}$'

if re.match(pattern,phone):
     print('valid indian phone number')
else:
     print('invalid phone number')
