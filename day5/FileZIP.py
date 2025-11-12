#create a zip file

import zipfile

# with zipfile.ZipFile('file.zip', 'w') as z:
#      z.write('number.py')
#      z.write('pathFinder.py')

# print('zip file created')


#display the list of files in the zip archive

# with zipfile.ZipFile('file.zip', 'r') as z:
#      print(z.namelist())


#extract a single file from the zip archive

with zipfile.ZipFile('file.zip', 'r') as z:
     z.extract('number.py')