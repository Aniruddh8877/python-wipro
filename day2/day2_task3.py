#library book tracking and late fee management

issue_books={
     
'm-102':['python basic','ai fundamentals'],
'm-205':['data science','os concepts','python basic'],
'm-310':['dbms principles','computer network','ai fundamentals']
}

reference_books={'python basic','dbms principles'}

late_fee_member =[]

for member_id,books in issue_books.items():
     if 'python basic' not in books:
        print("{} missed required reference book.".format(member_id))

     if len(books)>=3:
        late_fee_member.append(member_id)

member_tuple = tuple(issue_books.keys())
audit_code = '#'.join(member_tuple)
sliced_code = audit_code[2:9]
final_code = sliced_code.upper()

print("\n------- library audit report----------------")
print("total member with late fee:{}".format(len(late_fee_member)))
print("final uppercase audit code:{}".format(final_code))
print("late fee member: {}".format(late_fee_member))