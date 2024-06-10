#generate random int (1~100)
#let user repeat input
#if right, print ('you got it')
#if not right, tell him bigger or smaller

import random

start = input ('please give lower: ')
end = input ('please give upper: ')
start = int(start)
end = int (end) 

r = random.randint(start, end)
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

