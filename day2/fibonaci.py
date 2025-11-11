#fibonacci sequence

n = int(input("Enter the number:"))
prev =0
current =1
print(prev,end=' ')
print(current,end=' ')
count =2
while count <= n:
     result =current + prev
     print(result, end=' ')
     prev = current
     current = result
     count += 1

print("Fibonacci sequence up to", n, "terms is printed above.")