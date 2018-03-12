#CLCSFast 

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

# Compute shortest path of mid (pm) using dynamic programming bounded by pl and pu
def SingleShortestPath(A,B,mid,pl,pu):
	 # find most optimal path from (mid,0) to (mid+m, n)
	 # Store an array of paths then choose the shortest one
	 # Every time you look at a node check if it is in the bounds 
	 # Basically LCS but when we hit a bound use the bound path 

	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])
	return arr[m][n]



def FindShortestPath(A,B,p,l,u):
     if (u-l <= 1) return
     mid = (l+u)/2
     p[mid] = SingleShortestPath(A,B,mid,p[l],p[u])
     FindShortestPath(A,B,p,l,mid)
     FindShortestPath(A,B,p,mid,u)
     


def CLCSFast(A,B):
	m = len(A)
	n = len(B)
    p = [][]# array of arrays to represent paths?
    FindShortestPath(A,B,p,0,m)



def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		print LCS(A,B)
	return

if __name__ == '__main__':
	main()