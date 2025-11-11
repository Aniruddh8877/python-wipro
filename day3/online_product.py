'''
an e-commerce platform wants to manage product tags for its item .
tags help in searching and filterin products, and duplicate tags should be avoided

the system should be able to:
add new tags to a product.
remove tags from a product.
check if a tag is associated with a product.
find all unique tags across multiple products.
identify common tags shared by two products.

using set is ideal becaue they automaticallly prevent duplicate
tags and allow operateion like union and intersection and 
membership checks efficiently.
'''


product_tags1 = {"electronics", "laptop", "gaming", "newarrival"}
product_tags2= {"laptop",'office','electronics','discount'}
print("Initial product tags:", product_tags1,"\n")
print("Initial product tags:", product_tags2,"\n")

#add new tag
product_tags1.add("portable")
print("after adding new tag:", product_tags1,"\n")

#remove the tag
product_tags1.remove("newarrival")
print('after removeing tags',product_tags1,"\n")

#check if gaming is a tag form product1
print('is gaming is a part of product1','gaming' in product_tags1,"\n")

#find all unique tags across multiple products
all_unique_tags = product_tags1.union(product_tags2)
print("all unique tags across both products:", all_unique_tags,"\n")

#identify common tags shared by two products
common_tags = product_tags1.intersection(product_tags2)
print("common tags shared by both products:", common_tags,"\n")