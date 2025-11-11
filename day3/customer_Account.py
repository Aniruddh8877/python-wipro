#a bank want to manage its cusitomer accounts
#using a digital system, eaxxh customer has 
#account number, name,account type,balance


customer_account = {
     101: {'name':'aniruddh','account_type':'savings','balance':5000},
     102: {'name':'bob','account_type':'current','balance':12000},
     103: {'name':'charlie','account_type':'savings','balance':7000},
     104: {'name':'diana','account_type':'current','balance':15000},
}

#action to perform on the cust acc
#deposit money
customer_account[101]['balance'] += 2000
print("after deposit,aniruddh's balance:",customer_account[101]['balance'],"\n")

#withdraw money
withdraw_amount = 3000
customer_account[102]['balance'] -= withdraw_amount
print("after withdraw,bob's balance:",customer_account[102]['balance'],"\n")

#add a new customer
customer_account[105] = {'name':'eva','account_type':'savings','balance':8000}
print('after adding new customer eva:',customer_account[105],"\n")

#close an account
customer_account.pop(103)
print('after closing charlie account:',customer_account,"\n")



# print("all customer account details:",customer_account)

for acc_no,details in customer_account.items():
    print("account number:{} , name:{} , account type:{} , balance:{}".format(
        acc_no,details['name'],details['account_type'],details['balance']
    ))

