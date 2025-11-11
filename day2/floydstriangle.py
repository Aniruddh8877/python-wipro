'''
    1
   2 3
  4 5 6
 7 8 9 10
'''


n = int(input("enter the number of rows :"))

# i=0
# j=0
# for i in range(0,n+1):
#     for j in range(1,n-i+1):
#         print('',end=' ')

#     for j in range(0,i+1):
#         print(i+j,end=' ')
#     print()


num =1
for i in range(1,n+1):
     for space in range(i,n):
          print('',end=' ')
     for j in range(1,i+1):
          print(num,end =' ')
          num +=1
     print()