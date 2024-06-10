#generate random int (1~100)
#let user repeat input
#if right, print ('you got it')
#if not right, tell him bigger or smaller

import random
r = random.randint(1, 100)
count = 0  #想把猜幾次建出

while True:
	count = count + 1 # 也可以寫成 "count += 1"
	num = input ('guess: ')
	num = int (num)
	if num == r:
		print ('you got it')
		print ('this is', count, 'times')
		break
	elif num > r:
		print  ('bigger than answer')
	elif num < r:
		print ('smaller than answer')
	print ('this is', count, 'times')

