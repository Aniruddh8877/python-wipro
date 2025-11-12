import re

#email = abc@exapmle.com
#email = abc.bca@gmai.com
#email = abc@ex-ample.org
#email= abc@123.com
#email = alice@example.in
#email= ANIRUDDH@EXAMPLE.COM  

email = 'aniruddh.abc@gmail.com'
pattern = r'^[A-z0-9\.-]+@[a-z0-9\.-]+\.[a-z]{2,}$'


if re.match(pattern,email,re.IGNORECASE):
     print('Valid email address')
else:
     print(' Invalid email address')
