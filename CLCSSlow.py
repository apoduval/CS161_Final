#CLCSSlow Implementation
import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

def cut(A,k):
	n  = len(A)
	if k < 0 | k >= n:
		k = k % n
	return  A[k:n] + A[0:k] #substring(A,k,n) + substring(A,0,k);

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

# Only cut over one of the strings while keeping the other one fixed
# do not zero/reset the DP array between calls to the LCS method 
def CLCSSlow(A,B):
	m = len(A)
	n = len(B)
	arr = []
	for i in range(0, m):
		arr.append(LCS(cut(A,i), B)) 
	return arr[np.argmax(arr)]

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	for l in sys.stdin:
		A,B = l.split()
		print(CLCSSlow(A,B))
	return

if __name__ == '__main__':
	main()
