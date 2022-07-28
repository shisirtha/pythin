import random
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
symbol = "!@#$%&*"
number = "0123456789"

Use_for = uppercase+ lowercase + symbol+ number
lenths = 8

password = "".join(random.sample(Use_for, lenths))

print("the password is " ,password)