f = open('demo.txt','r')
print(f.read())
f.close

print(f.readline())

for i in f:
     print(i)


# f1 = open('demo.txt','a')
# f1.write('\n this is the new file created by me')

# f1.close