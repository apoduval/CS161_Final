#CLCSFast
import sys
import numpy as np

arraySize = 20
arr = np.zeros((2*arraySize,arraySize), dtype=int)

p = [[[]]]

maxLCS = -1


def LCS(A,B):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return PathBacktrace(A + A,B, 0, -1, -1)

def PathBacktrace(A,B, mid, l, u):
	global maxLCS


	m = len(A)/2
	index = m

	i = mid + m
	j = len(B)


	#initialize boolean such that we check bounds even if top/bottom
	if l == -1 and u == -1:
		checkTop = 1
		checkLeft = 1
	else:
		checkTop = 0
		checkLeft = 0

	path = [[0,0] for x in range(m+ 1)]
	path[index] = [j,j]


	#SET MAX VALUE
	curr = arr[i][j]

	if curr > maxLCS:
		maxLCS = curr

	#recurse to backtrace
	while i>=0 and j >=0 and index >= 0:

		if i == 0 or j == 0 or index == 1:
			break

		curr = arr[i][j]
		diag = arr[i - 1][j - 1]
		left = arr[i][j-1]
		top = arr[i-1][j]

		if checkTop == 0:

			val =  p[l][index][1]
			if j <= val:
				checkTop = (j <= val)

		if checkLeft == 0:

			val =  p[u][index][0]
			checkLeft = (j >= p[u][index][0])

		#first check top
		if curr == top and checkTop:
			path[index-1] = [j,j]
			index = index - 1
			i= i-1

		#next check left
		elif curr == left and checkLeft:
			path[index][0] = j-1
			j=j-1

		#finally check diagonal
		elif diag == curr-1:
			path[index-1] = [j-1,j-1]
			index = index - 1
			i = i - 1
			j = j - 1



		#reset boolean values
		if l != -1 and u != -1:
			checkTop = 0
			checkLeft = 0

	return path



def SingleShortestPath(A,B,mid,l,u):

	global p
	global arr


	m = len(A)/2
	n = len(B)
	A_str_curr = A[mid:mid+m]

	#this clears the row before
	arr[mid] = np.zeros(arraySize, dtype=int)
	for i in range(1,m +1):
		index = mid + i

		leftBound = 1
		rightBound = n

		if index >= (u + 1):
			leftBound = p[u][index - (u +1) + 1][0]

		if index <= l + m:

			rightBound = p[l][index-l][1]

		if leftBound == 0:
			leftBound = 1
		if rightBound == 0:
			rightBound = 1
		jrange = range(leftBound,rightBound + 1)


		for j in jrange:

			if A[index-1] == B[j-1]: # If we have a match
				arr[index][j] = arr[index-1][j-1]+1
			else:
				arr[index][j] = max(arr[index-1][j], arr[index][j-1])

	return PathBacktrace(A,B, mid, l, u)

def FindShortestPath(A,B, l,u):

	A_double = A + A
	if (u-l <= 1):
		return
	mid = (l+u)/2

	p[mid] = SingleShortestPath(A_double,B,mid,l,u)
	FindShortestPath(A,B,l,mid)
	FindShortestPath(A,B,mid,u)

def ComputeP0_Pm(A,B):
	global p
	p[0] = LCS(A,B)
	p[len(A)] = p[0]

def CLCSFast(A,B):
	#define global variables
	global p
	global maxLCS
	global arr

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array
	p = np.zeros((m+1,m+1,2), dtype=int)
	arr = np.zeros((2*arraySize,arraySize), dtype=int)

	#initialize P0 and PM to hold LCS values
	ComputeP0_Pm(A,B)

	FindShortestPath(A,B,0,m)
	return maxLCS


def main():
	#print CLCSFast("ABGD", "ABCD")
	A = "BBAA"
	B = "ABABB"
	print "for strings:", A, B, "the answer is", CLCSFast(A, B)

	print CLCSFast("C","CDCCCEDBDEADEACDEBAEDDEAEAADCAEDAD")
	print CLCSFast("EBADAEEABBBCEDE", "ACBAAABDCAEADCEEBBDADDCEBCADCAEBBCDCAEDAC")
	print CLCSFast("ACBBBCDCEDBADBBEABBEDAEADEBAEB", "AEBEEAEEABAEEBCACDBBAEABCEDCABEEDACEEC")


if __name__ == '__main__':
	main()
