#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

def print_matrix1(a,x,y):
	mrows = len(x)
	ncols = len(y)

	print(" ", end=' ')
	print(" ", end='  ')
	for letter in range(ncols):
			print("%2c" % y[letter], end=' ')
	print()
	for i in range(mrows+1):
		if(i>0):
			print(x[i-1], end=' ')

		for j in range(ncols+1):
			if(i==0 and j==0):
				print(" ", end=' ')
			print("%2d" % a[i][j], end=' ')
		print()


def gen_matrix(x, y, match_score=3, gap_cost=2):
	mrows = len(x)
	ncols = len(y)

	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	# print_matrix1(a,x,y)
	# print()
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)
			# print_matrix1(a,x,y)
			# print()

	#print_matrix(a,x,y)
	return(a)

def check_pair(a, x, y):
	top = ""
	mid = ""
	bot = ""
	score = 3
	row = 2
	check = True

	for i in range(2,len(y)):
		for j in range(i-1,i+2):
			# print(i, j, a[i][j])
			if(a[i][j] == score):
				top = top + y[j-1] + " "
				mid = mid + "| "
				bot = bot + x[row-1] + " "
				row = row + 1
				score = score + 3
				check = False
		if(check):
			score = score - 3 - 2
			for k in range(i-1, i+2):
				if(a[i][k] == score):
					top = top + "- "
					mid = mid + "  "
					bot = bot + x[k] + " "
					score = score + 3
					row = row + 1
					check = False
		check = True

	print()
	print(top)
	print(mid)
	print(bot)

			
	
x = "GGTTGACTA"	
y = "TGTTACGG"

a=gen_matrix(x,y)

print_matrix1(a,x,y)
check_pair(a,x,y)









