# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 21:12:00 2018

@author: Hassan
"""
import math
import random

possible_num = []
while True:
    choice = int(input("Enter \n '1' For Unique credit card number input \n '2' for random number.\n"))
    if(choice == 1):
        credit_card_num = int(input("Enter Credit card number : "))
    if(choice == 2):
        credit_card_num = random.randint(int(10**15),int(10**16))
    if(int(math.log10(credit_card_num)) > 16 or int(math.log10(credit_card_num)) < 15 ):
        print("Invalid Credit Card Number.\nTRY AGAIN.")
    else:
        break
print("Your Credit Card Number is : " + str(credit_card_num))
while True:
    last = int(input("Enter number of digits to remove : "))
    if(last<10 and last > 0):
        break
    print("Invalid input Number.\nTRY AGAIN.")
initial = int((credit_card_num)/(int(pow(10,last)))) * (int(pow(10,last)))
last_pow10 = int(pow(10,last))
for comb in range(0,last_pow10):
    
    num_input = initial + comb
    str_input = str(num_input)
    list_input = list(str_input)
    
    sum_even = 0 
    sum_odd = 0
    sum_total = 0
    
    for i in range(0,16):
        if(i%2 == 0):
            temp = 0
            temp = int(list_input[i]) * 2
            if(temp >= 10):
                one_dig_temp = int(temp%10) + (int(temp/10))
            else:
                one_dig_temp = temp
            sum_even = sum_even + one_dig_temp  
        else:
            temp = 0
            temp = int(list_input[i])
            sum_odd = sum_odd + temp
    
    sum_total = sum_even + sum_odd
    if(sum_total % 10 == 0):
        possible_num.append(num_input)
print(possible_num)
print("Possible Last 4 digit combinations : "+str(len(possible_num)))
