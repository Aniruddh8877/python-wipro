# import re
# txt = 'The rain in Spain' #even a fullstop muct match

# x = re.search('^The.*Spain$',txt)

# if x:
#      print('yes ! we have a match')
# else:
#      print("we don't have hatch")


#extract all number from a text

import re
txt =' The order IDs are 12345,67890 and 22334'

number = re.findall(r'\d+',txt)

print(' extracted number',number)