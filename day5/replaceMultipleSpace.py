#replace multiple space with a single space

#strip = remove starting and end space

# import re
# txt='Hello          welcome         to         Python'
# cleaned_txt = re.sub(r'\s+'," ",txt)

# print('before',txt)
# print("after",cleaned_txt)

# \b = like boundare starting and ending boundary
#extract all word starting wiht capital letter 

import re
txt = "Python is created by Guido van Rossum in the Netherlands"
capital = re.findall(r'\b[A-Z][A-z]*\b',txt)
print(capital)