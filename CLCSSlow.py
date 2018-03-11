#CLCSSlow Implementation
import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

def cut(A,k):
	n  = len(A)
	if k < 0 | k >= n:
		k = k % n
	return  A[k:n] + A[0:k] #substring(A,k,n) + substring(A,0,k);

# Only cut over one of the strings while keeping the other one fixed
# do not zero/reset the DP array between calls to the LCS method -- do we even need a dp array?
def CLCSSlow():
	dpArr = []
	max = 0
	for i in range(0, m):
		for j in range(0, n):
		 	x = LCS(cut(A,k), cut(B,0)) # WHAT DO WE MAKE k?? 
		 	if x > max:
		 		max = x

# Returns the length of the LCS
def LCS(A,B):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return arr[m][n]

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	print(LCS("abcb","bdcab"))
	return

if __name__ == '__main__':
	main()
