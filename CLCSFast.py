#CLCSFast
import sys
import numpy as np

#initialize dp array to be 500x 500 because that is max string length
#initialize path to empty 2d array (will be initialized by size later)
#IMPORTANT NOTE: NEED A WAY TO CLEAR RELEVANT LENGTHS BETWEEN DIFFERENT STRING INPUTS
arr = np.zeros((20,10), dtype=int)

#path is 2 concatenated arrays to represent upper and lower bounds
p = [[]]
#make path an array of coordinate pairs????
LCS = []

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

#path holds index of B string associated with each possible m value

def PathBacktrace():
	return 0

def SingleShortestPath(A,B,mid,pl,pu):
	m = len(A)
	n = len(B)
	print "A double", A
	path = [0 for i in range(n)]
	print "pl is", pl
	print "pu is", pu

	for i in range(1,m/2 +1):
		index = mid + i
		print "char is", A[index]
		for j in range(1,n-1):
			if  (index >= pl[j] and index <= pu[j]) or (sum(pl) + sum(pu) == 0):
				if A[index-1] == B[j-1]:
					print "!!!!! match when these two char:", A[index-1], B[j-1]
					arr[index][j] = arr[index-1][j-1]+1
				else:
					print "NO match when these two char:", A[index-1], B[j-1]
					arr[index][j] = max(arr[index-1][j], arr[index][j-1])
	print arr
	#path = PathBacktrace()

	return path



	# # print "p is", p
	# # print "l is", l#, "pl is",  pl
	# # print "u is", u#, "pu is", pu
	# pl = p[l]
	# pu = p[(u - 1)]
	# print "A mid is", A[mid]
	# for i in range(1, m + 1): # keep the same should it be mid to mid+m?
	# 	index =  mid+i -m if mid + i >= m else mid + i
	# 	print "index is", index
	# 	print ""
	# 	for j in range(1,n+1):      #(1,n+1):
	# 		#if (j <= u) & (j >= l):
	# 		print "A char is,", A[index -1], "B char is,", B[j -1]
	# 		if A[index-1] == B[j-1]:
	# 			print "     match here:", A[index-1], "and", B[j-1]
	# 			arr[index][j] = arr[index-1][j-1]+1
	# 		else:
	# 			print "     no match:", A[index-1], "and", B[j-1]
	# 			arr[index][j] = max(arr[index-1][j], arr[index][j-1])
	# 			if arr[index][j] == arr[index][j-1]:
	# 				#path[index] = j-1
	# 		#path[index] = j
	# 	#print "path is"
	# 	#print path
	# 	print "arr is now"
	# 	print arr
	# return path
	#return arr[mid+m][n] #NEED TO RETURN AN ARRAY NOT A NUMBER



def FindShortestPath(A,B,p, l,u):
	 if (u-l <= 1):
		return
	 mid = (l+u)/2
	 print "mid is", mid, "l is", l, "u is", u
	 p[0][1] = [0, 1, 2, 3, 3]
	 p[1][1] = [0, 1, 2, 2, 3]
	 p[0][2] = [0, 3, 4, 4, 4]
	 p[1][2] = [0, 2, 4, 4, 4]
	 p[0][3] =  p[1][3]  = [0, 3, 4, 5, 5]

	 print p
	 #do we need all 4 upper and lower combos
	 #SingleShortestPath(A + A,B,mid,p[0][l],p[1][u])
	 #FindShortestPath(A,B,p,l,mid)
	 FindShortestPath(A,B,p,mid,u)


def CLCSFast(A,B):
	m = len(A)
	n = len(B)
	#need to figure out if + 1 or not

	path_l = path_u = np.zeros((m + 1,n+1), dtype=int)
	#path_l = path_u = [[0 for i in range(n+ 1)] for j in range(m)] # needs to be a gloabl variable
	p = [path_l, path_u]
	FindShortestPath(A,B,p,0,m)
	# Find the shortest pi from p
	min = p[0]


def main():
	print CLCSFast("AFG", "ABCD")
if __name__ == '__main__':
	main()
