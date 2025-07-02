import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

s = list(s1+s2+s3+s4)
random.shuffle(s)
passLen = int(input("Enter the length of password : "))

print("Password : ",''.join(random.sample(s , passLen)))
