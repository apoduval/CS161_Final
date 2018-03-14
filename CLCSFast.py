#CLCSFast
import sys
import numpy as np


arr = np.zeros((2000,4000), dtype=int)

p = [[[]]]

maxLCS = -1


#important note, we would only need mid,l,u if we wanted to compare to path
def PathBacktrace(A,B,mid,l,u):
	i = len(A)
	j = len(B)

	path = [[0,0] for x in range(m + 1)]

	path[i] =  [j,j]
	print "path is", path
	while i>=0 or j >=0: 
		cur = arr[i][j]
		#edge cases
		#if we are in [0,0], we exit the while loop
		if i == 0 and j == 0:
			break

		#if we are in the first row, go left
		elif i == 0 and j != 0: 
			path[i][0] = [j-1]
			j -= 1

		#if we are in the first col, go up
		elif i = 0 and j != 0: 
			path[i-1] = [j][j]
			i -= 1

		elif i >= 1 and j >= 1:
			diag = arr[i - 1][j - 1]
			left = arr[i - 1][j]
			top = arr[i][j-1]
			if A[i] == B[j]:
				path[i-1] = [j-1][j-1]
				i -= 1
				j -= 1
			# If not same, then find the larger of two and
	        # go in the direction of larger value
	        elif left >= top:
	        	path[i][0] = [j-1]
	            j-=1
	        else:
	        	path[i-1] = [j][j]
	            i-=1	

	return path



def SingleShortestPath(A,B,mid, l, u):

	global p
	global arr

	m = len(A)/2
	n = len(B)

	path = [0 for i in range(n)]

	for i in range(1,m +1):
		index = mid + i
		#print "char is", A[index]
		for j in range(1,n+1):
			#print "index is", index, "upper is", pu[j], "lower is", pl[j]
			#NOTE: BELOW WORKS FINE AND IS INDEED FASTER--GETS WEIRD WITH UPPER (original line
			# is the one under it)--Liv
			if  (index >= pl0[j]) or noPath:
			#if  (index >= pl m[j] and index <= pu[j]) or noPath:
				if A[index-1] == B[j-1]:
					#print "!!!!! match when these two char:", A[index-1], B[j-1]
					arr[index][j] = arr[index-1][j-1]+1
				else:
					#print "NO match when these two char:", A[index-1], B[j-1]
					arr[index][j] = max(arr[index-1][j], arr[index][j-1])
	#print "arr"
	#print arr
	# print
	# print
	print "LCS of this sequence is", arr[m + mid][n]
	LCS[mid] = arr[m + mid][n]
	#print "LCS is"
	#print LCS
	path = PathBacktrace(mid,m,l,u)

	return

# def FindShortestPath(A,B,p, l,u):
def FindShortestPath(A,B, l,u):
	 A_double = A + A
	 if (u-l <= 1): 
		return
	 mid = (l+u)/2

	 SingleShortestPath(A_double,B,mid,l,u)
	 FindShortestPath(A,B,l,mid)
	 FindShortestPath(A,B,mid,u)

def LCS(A,B):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return PathBacktrace(A,B)

def ComputeP0(A,B):
	p[0] = LCS(A,B)

def ComputePm(A,B):
	m = len(A)
	p[m] = LCS(A[m] + A[:m-1],B)

def CLCSFast(A,B):
	#define global variables
	global p
	global maxLCS

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array
	p = np.zeros(m,m, dtype=[]) #NOT SURE ABOUT DTYPE
	ComputeP0(A,B)
	#ComputePm(A,B)
	#FindShortestPath(A,B,0,m) 
	return maxLCS


def main():
	print CLCSFast("ABGD", "ABCD")
if __name__ == '__main__':
	main()
