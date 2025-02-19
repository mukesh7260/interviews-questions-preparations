# import re

# n = input('Enter mobile number: ')
# pattern = re.compile(r"^(?:\+91|91|0)?[-\s]?[7-9][0-9]{9}$")
# if pattern.match(n):
#     print(f'{n} is a valid mobile number')
# else:
#     print(f'{n} is not a valid mobile number')



import re

n = input('Enter mobile number: ')
pattern = re.compile(r"^(?:\+91|91|0)?[\s]?[7-9][0-9]{9}$")

# +91|91|0 ke sath yadi dash aata h tb -\s remove kr dega yadi nahi aaya tb start from number . 
if pattern.match(n):
    print(f'{n} is a valid mobile number')
else:
    print(f'{n} is not a valid mobile number')