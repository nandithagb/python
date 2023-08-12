import re
phone=(input("enter the number"))
phone_num=re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
if phone_num.match(phone):
    print("valid")
else:
    print("invalid")