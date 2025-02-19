# import re

# s = input('inter mobile number : ')
# f = re.match(r"(?:\+91|91|0)?[\s]?[7-9][0-9]{9}",s)

# if f:   
#     print('valid mobile number')
# else:
#     print('invalid mobile number')



import re

email = input("Enter email address: ")
# regex = "^[A-Z0-9.%+-]+@[A-Z0-9]+\.[A-Z]{2,}$"
regex = r"^[\w.%+-]+@[A-Za-z0-9]+\.[A-Za-z]{3,}$"
if len(email) > 7 and re.match(regex, email, re.IGNORECASE) is not None:
    print("Valid email address")
else:
    print("Invalid email address")