                         #Setup 

import random

import time

import string

imp_let = string.ascii_letters

imp_sym = string.punctuation

imp_num = string.digits

      #___________________________#
print ("")
print ("=" * 38)
print (" Welcome to password generator ".center (38, "="))
print ("=" * 38)
print ("\n")

print ("=" * 38)
length = int(input ("please type the lenght of the password :\n ")) 

print ("=" * 39)
letters = int(input ("How many letters do you want :\n  "))

print ("=" * 39)
num = int(input ("How many numbers do you want :\n "))

print ("=" * 39)
sym = int(input ("How many symbols do you want :\n ")) 

sum = sym + num + letters 

if length !=  sum :
	
	print (""" 
Error in length : 
the numbers, symbols and
letter not equal the length
of the password please try again 
	""")
else :
	
	random_etc = (
	random.choices (imp_let, k= (letters)) +
	random.choices (imp_num, k= (num)) +
	random.choices (imp_sym, k= (sym))
	)
	
	random.shuffle (random_etc)
	
	password = "".join (random_etc)
	
	print ("\nMaking the password ....")
	
	time.sleep (2) 
	
	print ("\n Here is the password \n")
	
	print ("=" * 20)
	print ("")
	print (password)
	print ("")
	print ("=" * 20)