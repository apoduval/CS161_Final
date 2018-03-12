#CLCSFast 
import sys
import numpy as np

arr = np.zeros((2048,2048), dtype=int)
p = [[]]

# Returns the length of the LCS
# def LCS(A,B):
# 	m = len(A)
# 	n = len(B)

# 	for i in range(1,m+1):
# 		for j in range(1,n+1):
# 			if A[i-1] == B[j-1]:
# 				arr[i][j] = arr[i-1][j-1]+1
# 			else:
# 				arr[i][j] = max(arr[i-1][j], arr[i][j-1])
# 	return arr[m][n]

# Compute shortest path of mid (pm) using dynamic programming bounded by pl and pu
# find most optimal path from (mid,0) to (mid+m, n)
# Store an array of paths then choose the shortest one
# Every time you look at a node check if it is in the bounds 
# Basically LCS but when we hit a bound use the bound path 
# arr[i][j] returns the length of the LCS 
def SingleShortestPath(A,B,mid,pl,pu):
	m = len(A)
	n = len(B)
	print "pl is",  pl
	print "pu is", pu
	path = [0 for i in range(m)]
	for i in range(m): # keep the same should it be mid to mid+m?
		index =  mid+i -m if mid + i >= m else mid + i
		l = pl[index]
		u = pu[index]
		print "char", A[index]
		for j in range(1,n+1):      #(1,n+1):
			if (j <= u) & (j >= l):
				if A[index-1] == B[j-1]:
					arr[index][j] = arr[index-1][j-1]+1
				else:
					arr[index][j] = max(arr[index-1][j], arr[index][j-1])
					if arr[index][j] == arr[index][j-1]:
						path[index] = j-1
				path[index] = j
	print "path is", path
	return path		
	#return arr[mid+m][n] #NEED TO RETURN AN ARRAY NOT A NUMBER 



def FindShortestPath(A,B,p,l,u):
	 if (u-l <= 1):
		return
	 mid = (l+u)/2
	 print "mid is", mid, "l is", l, "u is", u
	 p[mid] = SingleShortestPath(A,B,mid,p[l],p[u])
	 FindShortestPath(A,B,p,l,mid)
	 FindShortestPath(A,B,p,mid,u)
	 


def CLCSFast(A,B):
	m = len(A)
	n = len(B)
	p = [[0 for i in range(m+1)] for j in range(m+1)] # needs to be a gloabl variable
	FindShortestPath(A,B,p,0,m)
	# Find the shortest pi from p
	min = p[0]




def main():
	print CLCSFast("ABCDE", "ABABB")
if __name__ == '__main__':
	main()