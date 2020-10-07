# Katheryn Busch PSID: 1868948
# Coding Problem #2 CIS 2348 Homework 2

password = input()
new_password = ""
# change certain characters of the password 
for k in password:
   if k == 'i':
       new_password = new_password + '!'

   elif k == 'm':
       new_password = new_password + 'M'

   elif k == 'a':
       new_password = new_password + '@'

   elif k == 'B':
       new_password = new_password + '8'

   elif k == 'o':
       new_password = new_password + '.'

   else:
       new_password = new_password + k

new_password = new_password + "q*s"
print(new_password)