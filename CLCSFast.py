#CLCSFast
import sys
import numpy as np


arr = np.zeros((2000,4000), dtype=int)

p = [[[]]]

maxLCS = -1


def PathBacktrace(A,B,mid,l,u):
	i = len(A)/2
	j = len(B)

	path = []
	
	while i>=0 or j >=0: 
		cur = arr[i][j]

		if i == 0 and j == 0:
			break

		elif i == 0 and j != 0: # Go left 
			path += arr[i - 1][j]
			i -= 1

		elif i = 0 and j != 0: # Go up 
			path += arr[i][j-1]
			j -= 1

		elif i >= 1 and j >= 1:
			diag = arr[i - 1][j - 1]
			left = arr[i - 1][j]
			top = arr[i][j-1]
			if A[i] == B[j]:
				path += diag
				i -= 1
				j -= 1
			# If not same, then find the larger of two and
	        # go in the direction of larger value
	        elif left >= top:
	        	path += left
	            j-=1
	        else:
	        	path += top
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

def computeP0(A,B):
	LCS(A,B)


def CLCSFast(A,B):
	#define global variables
	global p
	global maxLCS

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array
	p = np.zeros(m,m, dtype=[]) #NOT SURE ABOUT DTYPE

	FindShortestPath(A,B,0,m) 
	return maxLCS


def main():
	print CLCSFast("ABGD", "ABCD")
if __name__ == '__main__':
	main()
