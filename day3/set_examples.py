'''
scenario
an online store want to store unique customer emails for 
sending promotional offers.email should not repeat
'''

#initial set of customer emails
customer_emails = {"pD5Bm@example.com","pD5Bm@example.com","5Vh4F@example.com","pD5Bm@example.com"}
# print("Initial customer emails:", customer_emails)


#adding new customer emails
customer_emails.add("b5EY5@example.com")
print("After adding new customer emails:", customer_emails)

#removing customer email 
customer_emails.remove("pD5Bm@example.com")
print("After removing a customer email:", customer_emails)

#check is an email is resigred
print("Is pD5Bm@example.com registered?", "b5EY5@example.com" in customer_emails)

#list all regisert email
print('registered emails',customer_emails)