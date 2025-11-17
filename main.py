# Random code generator

import random
# password="QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm123456789@/#-"
password="1234567890"

len_password=int(input("Enter The length of password : "))
a="".join(random.sample(password,len_password))
temp=a
# print(f"Your password is : {a}")
print(f"Your OTP is : {a}")

user_otp =int(input("Enter the otp : "))

while True:
    if user_otp == temp:
        print("Login successful")
        break
    else:
        print("Try again")
        user_otp = input("Enter OTP again: ")