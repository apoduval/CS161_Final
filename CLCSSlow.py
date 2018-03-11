#CLCSSlow Implementation
import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

def cut(A,k):
	n  = A.length()
	if k < 0 || k >= n:
		k = k%n

	return substring(A,k,n) + substring(A,0,k);

# Only cut over one of the strings while keeping the other one fixed
# do not zero/reset the DP array between calls to the LCS method 
# use Python string/list slicing for the cutting.
def CLCSSlow():
	for i in range(0, m): # should i start from 0 or 1?
		for j in range(0, n):
		 	LCS(cut(A,i), cut(B,j))


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
	
	for l in sys.stdin:
		A,B = l.split()
		print LCS(A,B)
	return

if __name__ == '__main__':
	main()
