import random

print("PASSWORD GENERATOR")

input("enter \'y\' to start : ")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'


number = int(input("number of passwords you want : "))

length = int(input("enter the length of each password : "))

for p in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print("password : ", password)



input("enter \'x\' to exit : ")