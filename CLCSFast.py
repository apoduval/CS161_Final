#CLCSFast
import sys
import numpy as np


arr = np.zeros((10,10), dtype=int)

p = [[[]]]

maxLCS = -1


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

#important note, we would only need mid,l,u if we wanted to compare to path
def PathBacktrace(A,B):
	#print arr
	#print "string A", A, "string B", B
	i = len(A)
	j = len(B)

	path = [[0,0] for x in range(i + 1)]

	path[i] =  [j,j]
	while i>=0 or j >=0: 
		#print "i is", i, "j is", j, "which are char", A[i-1], B[j-1]
		#print "path is", path
		cur = arr[i][j]
		#edge cases
		#if we are in [0,0], we exit the while loop
		if i == 0 and j == 0:
			break

		#if we are in the first row, go left
		elif i == 0 and j != 0: 
			#print "We are in first row, need to go left"
			path[i][0] = j-1
			j=j-1

		#if we are in the first col, go up
		elif j == 0 and i != 0: 
			#print "We are in first col, need to go up"
			path[i-1] = [j,j]
			i= i-1

		else: #i >= 1 and j >= 1:
			diag = arr[i - 1][j - 1]
			left = arr[i][j-1]
			top = arr[i-1][j]
			if (diag == cur - 1) and (A[i-1] == B[j-1]) :
				#print "MATCH!" #we are doing a diagonal", A[i-1], B[j-1]
				path[i-1] = [j-1,j-1]
				i = i - 1
				j = j - 1
			# If not same, then find the larger of two and
			# go in the direction of larger value
			elif left >= top:
				#print "No match. we are going left"
				path[i][0] = j-1
				j=j-1
			else:
				#print "No match. we are going up"
				path[i-1] = [j,j]
				i=i-1	

	return path



def SingleShortestPath(A,B,mid,l,u):
	global maxLCS
	print
	print
	print
	print
	print "ENTERING SSP"

	global p
	global arr

	#temporarily fix arr 

	m = len(A)/2
	n = len(B)		
	A_str_curr = A[mid:mid+m]
	print "STrings we are comparing:", A_str_curr, B


	for i in range(1,m +1):
		plRight = p[l][i][1] 
		puLeft = p[u][i][0] 

		jrange = (1,n)
		index = mid + i

		if index <= u and index >= l:
			jrange = (0,plRight)
		elif index > u and index > m:
			jrange = (puLeft,n)
		elif index > u:
			jrange = (puLeft, plRight)
		print "jrange is", jrange
		for j in jrange:
			#print "A", A[index -1]
			#print "B", B[j-1]
			if A[index-1] == B[j-1]: # If we have a match 
				arr[index][j] = arr[index-1][j-1]+1
			else:
				arr[index][j] = max(arr[index-1][j], arr[index][j-1])
	
	print "array when we do our method"
	print arr
	print
	print arr

	#LCS = arr[m + mid][n]
	#print "LCS value is"

	#if LCS > maxLCS:
	#	maxLCS = LCS
	return PathBacktrace(A,B)

# def FindShortestPath(A,B,p, l,u):
def FindShortestPath(A,B, l,u):
	 A_double = A + A
	 if (u-l <= 1): 
		return
	 mid = (l+u)/2

	 p[mid] = SingleShortestPath(A_double,B,mid,l,u)
	 FindShortestPath(A,B,l,mid)
	 FindShortestPath(A,B,mid,u)



def ComputeP0(A,B):
	p[0] = LCS(A,B)

def ComputePm(A,B):
	m = len(A)
	#print "first char", A[m-1]
	p[m] = LCS(A[m-1] + A[0:m-1],B)

def CLCSFast(A,B):
	#define global variables
	global p
	global maxLCS

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array

	p = np.zeros((m+1,m+1,2), dtype=int) #NOT SURE ABOUT DTYPE
	LCS("GDAB", "ABCD")
	print "LCS of GDAB is"
	print arr
	ComputeP0(A,B)
	ComputePm(A,B)
	#print "final path with 0 and m"
	#print p
	FindShortestPath(A,B,0,m) 

	return maxLCS


def main():
	print CLCSFast("ABGD", "ABCD")
if __name__ == '__main__':
	main()
