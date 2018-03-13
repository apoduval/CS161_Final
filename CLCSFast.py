#CLCSFast
import sys
import numpy as np

#initialize dp array to be 500x 500 because that is max string length
#initialize path to empty 2d array (will be initialized by size later)
#IMPORTANT NOTE: NEED A WAY TO CLEAR RELEVANT LENGTHS BETWEEN DIFFERENT STRING INPUTS
arr = np.zeros((10,10), dtype=int)

#path is 2 concatenated arrays to represent upper and lower bounds
p = [[[]],[[]]]
#make path an array of coordinate pairs????
LCS = []


# Compute shortest path of mid (pm) using dynamic programming bounded by pl and pu
# find most optimal path from (mid,0) to (mid+m, n)
# Store an array of paths then choose the shortest one
# Every time you look at a node check if it is in the bounds
# Basically LCS but when we hit a bound use the bound path
# arr[i][j] returns the length of the LCS

#path holds index of B string associated with each possible m value


#!!!!!WHAT WAS SAID DURING OFFICE HOURS!!!!!
#First check if you can take the diagonal! The only way you can take the diagonal
# is if the diagonal number is one less than your current number AND the chars are the same.
#If these both check out, take the diagonal.

#If not, check the top and left.
#If one is the same number as your cur, but the other isn't,
#you have to go in that direction.

#If both left and top are the same as your cur,
#you can take either!

#Make sure you never cross the lines--
# i. e., check your upper and lower bounds, and your horizontal bounds (m to mid+m).

def PathBacktrace(mid,m,l,u):
	#note: need to pass in arr
	#for (int i = m; i > 0; i++) :
	#  cur = arr[i][j]
	#  diag = arr[i - 1][j - 1]
	#  if (diag == cur - 1) && A[diag] == B[cur]:
	#	#if the diagonal is one less and the char is the same
	#    path += diag
	#	 i - 1; j - 1;
	#  else:
	#    left = arr[i - 1][j]
	#    top = arr[i][j-1]
	#      if (left == top == cur):
	#         #can go left or top
	#         path += left;
	#		  i - 1;
	#	   if (left = cur):
	#		path += left;
	#		i - 1;
	#		if (top = cur):
	#		path += top;
	#		j - 1;

	#first lower, first upper
	if mid == 1:
		 p[0][1] = [0, 1, 2, 3, 3]
		 p[1][1] = [0, 1, 2, 2, 3]
	#second lower, second upper
	elif mid == 2:
	 	p[0][2] = [0, 3, 4, 4, 4]
	 	p[1][2] = [0, 2, 4, 4, 4]
	#third lower and third upper
	else:
	    p[0][3] =  p[1][3]  = [0, 3, 4, 5, 5]


def SingleShortestPath(A,B,mid, l, u):

	global p
	global arr

	m = len(A)/2
	print "m",  m
	n = len(B)

	print "path"
	print p

	#set upper and lower path bounds
	noPath = (l == 0)

	#0 : lower, 1: upper
	pl0 = p[0][l]
	pl1 = p[1][l]
	pu0= p[0][u]
	pu1 = p[1][u]

	print "pl0", pl0
	#print "pl1", pl1
	print "pu0", pu0
	#print "pu1", pu1

	#iterate using dp array, within path bounds
	print "we are comparing these strings:", A[mid: mid + m], B
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
	print "arr"
	print arr
	print
	print
	print "LCS of this sequence is", arr[m + mid][n]
	LCS[mid] = arr[m + mid][n]
	print "LCS is"
	print LCS
	path = PathBacktrace(mid,m,l,u)

	return





# def FindShortestPath(A,B,p, l,u):
def FindShortestPath(A,B, l,u):
	 A_double = A + A
	 global p
	 if (u-l <= 1):
		return
	 mid = (l+u)/2
	 print "mid is", mid, "l is", l, "u is", u

	 SingleShortestPath(A_double,B,mid,l,u)
	 FindShortestPath(A,B,l,mid)
	 FindShortestPath(A,B,mid,u)


def CLCSFast(A,B):
	#define global variables
	global p
	global LCS

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array
	path_l = path_u = np.zeros((m + 1,n+1), dtype=int)
	p = [path_l, path_u]

	#initialize LCS array
	LCS = np.zeros(m + 1, dtype=int)

	#FindShortestPath(A,B,p,0,m)
	FindShortestPath(A,B,0,m)
	return max(LCS)


def main():
	print CLCSFast("ABG", "ABCD")
if __name__ == '__main__':
	main()
