#CLCSFast
import sys
import numpy as np


arr = np.zeros((100,100), dtype=int)

p = [[[]]]

maxLCS = -1


def LCS(A,B, start):
	m = len(A)/2
	n = len(B)

	#to avoid starting at a lower line
	if start > 0: start = start - 1
	
	#to zero the array row before so that LCS algorithm works
	arr[start] = np.zeros(100, dtype=int)

	for i in range(1,m+1):
		index = i + start
		for j in range(1,n+1):
			if A[index-1] == B[j-1]:
				arr[index][j] = arr[index-1][j-1]+1
			else:
				arr[index][j] = max(arr[index-1][j], arr[index][j-1])

	return PathBacktrace(A,B, start, -1, -1)

#important note, we would only need mid,l,u if we wanted to compare to path
def PathBacktrace(A,B, mid, l, u):
	global maxLCS
	#print arr
	#print "string A", A, "string B", B
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

	#set boolean variables 

	#SET MAX VALUE
	curr = arr[i][j]
	if curr > maxLCS:
		maxLCS = curr

	#recurse to backtrace
	while i>=0 and j >=0: 

		if i == 0 or j == 0:
			break

		curr = arr[i][j]
		diag = arr[i - 1][j - 1]
		left = arr[i][j-1]
		top = arr[i-1][j] 

		if checkTop == 0:
			checkTop = j <= path[l][1]

		if checkLeft == 0:
			checkLeft = (j >= path[l][0])

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

	print "the path we created is:"
	print path
	return path



def SingleShortestPath(A,B,mid,l,u):
	print
	print "ENTERING SSP"

	global p
	global arr


	m = len(A)/2
	n = len(B)
	print "This is the A string", A
	A_str_curr = A[mid:mid+m]
	print "Strings we are comparing:", A_str_curr, B

	arr[mid - 1] = np.zeros(100, dtype=int)

	for i in range(1,m +1):
		#print "mid is: ", mid, "l is:", l, "u is:", u
		plRight = p[l][i][1] 
		puLeft = p[u][i][0] 
		#print "plRight:", plRight
		#print "puLeft", puLeft

		jrange = (1,n)
		index = mid + i

		if index <= u and index >= l:
			jrange = range(1,plRight + 1)

		elif index > u and index > m:
			jrange = range(puLeft,n + 1)
		elif index > u:
			jrange = range(puLeft, plRight + 1)
#print "jrange is", jrange

		for j in jrange:
			#print "j here is", j
			#print "A", A[index -1]
			#print "B", B[j-1]
			if A[index-1] == B[j-1]: # If we have a match 
				arr[index][j] = arr[index-1][j-1]+1
			else:
				arr[index][j] = max(arr[index-1][j], arr[index][j-1])

	print
	print
	print "array when we do our method AT mid =", mid, A[mid], "l is:", l, A[l], "u is:", u, A[u]
	print arr
	print

	return PathBacktrace(A,B, mid, l, u)

# def FindShortestPath(A,B,p, l,u):
def FindShortestPath(A,B, l,u):
	A_double = A + A
	if (u-l <= 1): 
		return
	mid = (l+u)/2

	p[mid] = SingleShortestPath(A_double,B,mid,l,u)
	FindShortestPath(A,B,l,mid)
	FindShortestPath(A,B,mid,u)



def ComputeP0(A,B):
	print "Strings we are comparing:", A[0:len(A)/2], B
	p[0] = LCS(A,B,0)

def ComputePm(A,B):
	m = len(A)/2
	#print "first char", A[m-1]
	print "Strings we are comparing:", A[m:], B
	p[m] = LCS(A,B,m)

def CLCSFast(A,B):
	#define global variables
	global p
	global maxLCS
	global arr

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array
	p = np.zeros((m+1,m+1,2), dtype=int) #NOT SURE ABOUT DTYPE

	#initialize P0 and PM to hold LCS values
	ComputeP0(A+A,B)
	# print "the total path array is:"
	# print p

	ComputePm(A+A,B)
	# print "the total path array is:"
	# print p

	FindShortestPath(A,B,1,m)
	return maxLCS


def main():
	#print CLCSFast("ABGD", "ABCD")
	print CLCSFast("BBAA", "ABABB")
	#print CLCSFast("C","CDCCCEDBDEADEACDEBAEDDEAEAADCAEDAD")
	#print CLCSFast("EBADAEEABBBCEDE", "ACBAAABDCAEADCEEBBDADDCEBCADCAEBBCDCAEDAC")
	#print CLCSFast("ACBBBCDCEDBADBBEABBEDAEADEBAEB", "AEBEEAEEABAEEBCACDBBAEABCEDCABEEDACEEC")


if __name__ == '__main__':
	main()




