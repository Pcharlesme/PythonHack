# generate complex password 

import random

lower_case = "abcdefghijklmnopqrstvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTWXYZ "
number = "0123456789"
symbols = "!@#$%&*\?/+-_"
platform = input(" What is the platform name:") 
Use_for = lower_case + upper_case + number + symbols
length_for_pass = 12
password = "".join(random.sample(Use_for,length_for_pass))
print(platform)
print("Your generated password for " +platform ,"is :" +password)