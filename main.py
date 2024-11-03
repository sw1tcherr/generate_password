import random
sym = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("Введите желаемую длину пароля: "))
password = " "
for i in range(pass_len):
    password += random.choice(sym)
print(password) 
