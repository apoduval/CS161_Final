#CLCSFast
import sys
import numpy as np

arraySize = 5000
arr = np.zeros((2*arraySize,arraySize), dtype=int)

p = [[[]]]

maxLCS = -1

#important note, we would only need mid,l,u if we wanted to compare to path
def PathBacktrace(A,B, mid, l, u, jrange_arr):
	global maxLCS
	print "enter backtrace"

	m = len(A)/2
	index = m 


	print "string A", A[mid:mid+m], "string B", B
	print "the array is"	
	print arr[mid:mid + m + 1]

	i = mid + m  
	j = len(B)

	#initialize boolean such that we check bounds even if top/bottom 
	#p0 and pm automatically set to true 
	if l == -1 and u == -1:
		checkTop = 1
		checkLeft = 1
	else: 
		checkTop = 0
		checkLeft = 0

	path = [[0,0] for x in range(m+ 1)]
	path[index] = [j,j]


	#set boolean variables 

	#SET MAX VALUE
	curr = arr[i][j]

	if curr > maxLCS:
		maxLCS = curr
		print "Max LCS is", maxLCS


	#iterate and find path
	while i>=0 and j >=0 and index >= 0: 

		if i == 0 or j == 0 or index == 1:
			break

		curr = arr[i][j]

		diag = arr[i - 1][j - 1]
		left = arr[i][j-1]
		top = arr[i-1][j] 


		#MODIFY CHECK TOP AND LEFT BOOLEANS. If they are within bounds, set boolean to true
		if checkTop == 0:

			if j >= jrange_arr[index-1][0] and j <= jrange_arr[index-1][1]:
		#		print "checkTop is now true!"
				checkTop = 1

		if checkLeft == 0:
			if j - 1 >= jrange_arr[index][0]:
			#	print "checkleft is now true!"
				checkLeft = 1



		#LOGIC FOR BACKTRACE
		#First, prioritize top
		if curr == top and checkTop:
		#	print "went up"
			path[index-1] = [j,j]
			index = index - 1
			i= i-1

		#Next check left
		elif curr == left and checkLeft:
		#	print "---------------------went left"
			path[index][0] = j-1
			j=j-1
			#print "after, j value is", j


		#Finally check diagonal
		elif diag == curr-1:
			#print "went diag"
			path[index-1] = [j-1,j-1]
			index = index - 1
			i = i - 1
			j = j - 1

		#Reset boolean values if not P0
		if l != -1 and u != -1:
			checkTop = 0
			checkLeft = 0
	
	print "path is", path
	return path

def SingleShortestPath(A,B,mid,l,u):
	global p
	global arr


	m = len(A)/2
	n = len(B)

	A_str_curr = A[mid:mid+m]
	#print "Strings we are comparing:", A_str_curr, B

	#this clears the row before
	arr[mid] = np.zeros(arraySize, dtype=int)


	#Iniitialize jrange array: array that will hold our row values from path
	#set range of 0th row to include all possible outcomes since a node can end in the 0s row
	jrange_arr = [[0,0] for i in range(m + 1)]
	jrange_arr[0] = [0,n]


	for i in range(1,m +1):
		index = mid + i

		leftBound = 1
		rightBound = n

		if index >= u+1:
			leftBound = p[u][(index - u )][0]


		if index <= l + m:
			rightBound = p[l][index-l][0]

		#Adjust for 0s given that our dp has an extra column as a buffer
		if leftBound== 0:
			leftBound = 1

		if rightBound== 0:
			rightBound = 1

		#Store bounds into array and range for iteration
		jrange = range(leftBound,rightBound + 1)
		jrange_arr[i] = [leftBound, rightBound]
		#print "jrange is", jrange_arr
		#iterate through array to fill dynamic programming table arr
		for j in jrange:

			# If characters match have a match 
			if A[index-1] == B[j-1]:  

				#if the diagonal is in the jrange, make the current arr[index][j] equal to 1 + the diagonal (NORMAL CASE)
				if j-1 >= jrange_arr[i-1][0] and j-1 <= jrange_arr[i-1][1]:
					#print "case 1, match", A[index-1], B[j-1]
					#print "the array value am adding to is:", index-1, j-1
					arr[index][j] = arr[index-1][j-1]+1

				#EDGE CASE: if diagonal is in 0s row, add 1
				else:
					arr[index][j] = arr[index][j-1] + 1
					#print "case 2"
			
			# If characters don't match
			else:

				#if the value above is in legal territory, take the max (NORMAL CASE)
				#print "j", j, "greater than", jrange_arr[i-1][0], "less than", jrange_arr[i-1][1]
				if j >= jrange_arr[i-1][0] and j <= jrange_arr[i-1][1]:
				#	print "case 3"
					arr[index][j] = max(arr[index-1][j], arr[index][j-1])


				#EDGE CASE: if there is no match and the top is out of bounds, set value = to the left node
				else:
					#print "case 4"
					arr[index][j] = arr[index][j-1]
		
	#print "the array is"	
	#print arr[mid:mid + m + 1]
	return PathBacktrace(A,B, mid, l, u, jrange_arr)

def FindShortestPath(A,B, l,u):
	A_double = A + A
	if (u-l <= 1): 
		return
	mid = (l+u)/2 

	print "filling p of mid for mid", mid, "in string A, at char,", A[mid]

	p[mid] = SingleShortestPath(A_double,B,mid,l,u)

	#FindShortestPath(A,B,l,mid)
	#FindShortestPath(A,B,mid,u)

def LCS(A,B):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		#index = i + start
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return PathBacktrace(A + A,B, 0, -1, -1, 0)

def ComputeP0_Pm(A,B):
	global p
	p[0] = LCS(A,B)
	p[len(A)] = p[0]


def CLCSFast(A,B):
	#define global variables
	global p
	global maxLCS
	global arr

	#lengths of A and B
	m = len(A)
	n = len(B)

	#initialize path array
	p = np.zeros((m+1,m+1,2), dtype=int) #NOT SURE ABOUT DTYPE

	#initialize P0 and PM to hold LCS values
	ComputeP0_Pm(A,B)

	FindShortestPath(A,B,0,m)
	return maxLCS


def main():
	#print CLCSFast("ABGD", "ABCD")
	A = "ABABB " 
	B = "BBABABAAA"
	print "for strings:", A, B, "the answer is", CLCSFast(A, B)


if __name__ == '__main__':
	main()
