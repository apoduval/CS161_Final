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



def SingleShortestPath(A,B,mid,l,u):

	global p
	global arr

	m = len(A)/2
	n = len(B)

	#path = [0 for i in range(n)]


	for i in range(1,m +1):
		plRight = p[l][i][1] + 1 
		puLeft = p[u][i][0] + 1
		jrange = (1,n)
		index = mid + i

		if i <= u and i >= l:
			jrange = (1,plRight)
		elif i > u and i > m:
			jrange = (puLeft,n)
		elif i > u:
			jrange = (puLeft, plRight)

		for j in jrange:
			if A[index-1] == B[j-1]: # If we have a match 
				arr[index][j] = arr[index-1][j-1]+1
			else:
				arr[index][j] = max(arr[index-1][j], arr[index][j-1])
	print "LCS of this sequence is", arr[m + mid][n]

	path = PathBacktrace(A,B,mid,l,u)

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
	p = np.zeros(m,m, dtype= array) #NOT SURE ABOUT DTYPE

	FindShortestPath(A,B,0,m) 
	return maxLCS


def main():
	print CLCSFast("ABGD", "ABCD")
if __name__ == '__main__':
	main()
