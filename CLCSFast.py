#CLCSFast
import sys
import numpy as np


arr = np.zeros((10,10), dtype=int)

p = [[[]]]

maxLCS = -1


def LCS(A,B, start):
	m = len(A)/2
	n = len(B)

	for i in range(1,m+1):
		index = i + start
		for j in range(1,n+1):
			if A[index-1] == B[j-1]:
				arr[index][j] = arr[index-1][j-1]+1
			else:
				arr[index][j] = max(arr[index-1][j], arr[index][j-1])

	return PathBacktrace(A,B, start)

#important note, we would only need mid,l,u if we wanted to compare to path
def PathBacktrace(A,B, mid):
	#print arr
	#print "string A", A, "string B", B
	m = len(A)/2
	i = mid + m  #NOT SURE ABOUT THE -1 
	index = m 
	j = len(B)

	path = [[0,0] for x in range(m+ 1)]
	path[index] = [i,j]

	while i>0 and j >0: 

		print "i is", i, "j is", j, "which are char", A[i-1], B[j-1]
		#print "path is", path
		curr = arr[i][j]
		diag = arr[i - 1][j - 1]
		left = arr[i][j-1]
		top = arr[i-1][j] 

		if top == curr:
			#print "No match. we are going up"
			path[index-1] = [j,j]
			index = index - 1
			i= i-1
		elif diag == curr-1:
			#print "MATCH!" #we are doing a diagonal", A[i-1], B[j-1]
			path[index-1] = [j-1,j-1]
			index = index - 1
			i = i - 1
			j = j - 1
		else:
			#print "No match. we are going left"
			path[index][0] = j-1
			j=j-1

	print "the path we created is:"
	print path
	return path



def SingleShortestPath(A,B,mid,l,u):
	global maxLCS
	print
	print
	print "ENTERING SSP"

	global p
	global arr


	m = len(A)/2
	n = len(B)
	A_str_curr = A[mid:mid+m]
	print "Strings we are comparing:", A_str_curr, B

	for i in range(1,m +1):
		print "mid is: ", mid, "l is:", l, "u is:", u
		plRight = p[l][i][1] 
		puLeft = p[u][i][0] 
		print "plRight:", plRight
		print "puLeft", puLeft

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
	print "array when we do our method AT P", mid
	print arr
	print

	#LCS = arr[m + mid][n]
	#print "LCS value is"

	#if LCS > maxLCS:
	#maxLCS = LCS
	return PathBacktrace(A_,B, mid)

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
	p[0] = LCS(A,B,0)

def ComputePm(A,B):
	m = len(A)/2
	#print "first char", A[m-1]
	p[m] = LCS(A,B,m)

def CLCSFast(A,B):
	#print "empty array"
	#print arr
	#define global variables
	global p
	global maxLCS

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array

	p = np.zeros((m+1,m+1,2), dtype=int) #NOT SURE ABOUT DTYPE
	#LCS("GDAB", "ABCD")
	#print "LCS of GDAB is"
	#print arr
	ComputeP0(A+A,B)
	print "AFTER P0, ARRAY IS"
	print arr
	print
	print

	ComputePm(A+A,B)
	#print "final path with 0 and m"
	#print p
	print "AFTER PM, ARRAY IS"
	print arr
	print
	print
	FindShortestPath(A+A,B,1,m)
 

	return maxLCS


def main():
	print CLCSFast("ABGD", "ABCD")

if __name__ == '__main__':
	main()




