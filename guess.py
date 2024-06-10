#generate random int (1~100)
#let user repeat input
#if right, print ('you got it')
#if not right, tell him bigger or smaller

import random
r = random.randint(1, 100)
while True:
	num = input ('guess: ')
	num = int (num)
	if num == r:
		print ('you got it')
		break
	elif num > r:
		print  ('bigger than answer')
	elif num < r:
		print ('smaller than answer')

