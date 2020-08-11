
from decimal import *

def coinConvert(x):
	x = int(x * 100)
	#convert dollar amount into cent amount (no decimal)
	
	print(x // 25 , 'quarters') if x // 25 != 1 else print(
		'1 quarter')
	x %= 25
	#prints how many times 25 goes into inputAmount
	#x %= 25 changes inputAmount to the remaining bal

	print(x // 10 , 'dimes')if x // 10 != 1 else print(
		'1 dime')
	x %= 10
	#prints number of dimes

	print(x // 5 , 'nickles')if x // 5 != 1 else print(
		'1 nickle')
	x %= 5
	#prints number of nickles

	print(x , 'pennies')if x != 1 else print(
		'1 penny')
	#prints remaining pennies

	#def each coin to clean up functions in conditional statement


inputAmount = Decimal(input("Enter dollar amount: $"))

coinConvert(inputAmount)
