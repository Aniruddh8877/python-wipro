# scenorio : online shopping cart system

#initialize the cart

cart=['laptop','mouse','keyboard','charger','headphones','mouse']

# print("Initial cart items:",cart)

#add a new item to the cart

cart.append('usb cable')
print('after append',cart)

#insert an item at specific index
cart.insert(1,'headphone')
print('after inserting headphone at index 1:',cart,'\n')

#remove an item from the cart
cart.remove('mouse') #removes first occurance of mouse
print('after removing mouse:',cart,"\n")

#pop an item from the cart
pop_item= cart.pop() #removes last item if index not specified
print(pop_item,'is removed from the cart \n')
print('after popping an item:',cart,'\n')


#index() find th position of an item
position = cart.index('keyboard')
print('the index of keyboard is :',position,'\n')

#count() counts the occurance of an item
mouse_count = cart.count('mouse')
print('the count of mouse in the cart is :',mouse_count,'\n')
cart.append('mouse')
mouse_count2 = cart.count('mouse')
print('the count of mouse in the cart is :',mouse_count2,'\n')

dup = cart.copy()
print(dup,"jhgkjhgkjhgkjhhkgkhgkjhkg")
# sort the cart items
cart.sort()
print('after sorting the cart items :',cart,'\n')

#reverse sort the cart items
desc=sorted(dup,reverse=True)
print(desc)


#extend() to add multiple items to the cart
new_items = ['webcam','microphone']
cart.extend(new_items)
print('after extending the cart with new items:',cart,'\n')

#clear() to remove all items from the cart
dup.clear()
print('after clearing the cart:',dup,'\n')