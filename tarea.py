import random

digits = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("q tan larga quiers tu contraseña"))
password = ""


for i in range(length):
    password += random.choice(digits)
   
print (password)
