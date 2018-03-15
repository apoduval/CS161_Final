#CLCSFast
import sys
import numpy as np

arraySize = 20
arr = np.zeros((2*arraySize,arraySize), dtype=int)

p = [[[]]]

maxLCS = -1


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

	return PathBacktrace(A + A,B, 0, -1, -1)

#important note, we would only need mid,l,u if we wanted to compare to path
def PathBacktrace(A,B, mid, l, u):
	global maxLCS
	print "enter backtrace"
	#print arr
	print "string A", A, "string B", B


	m = len(A)/2
	index = m 

	i = mid + m  
	j = len(B)


	#initialize boolean such that we check bounds even if top/bottom
	if l == -1 and u == -1:
		checkTop = 1
		checkLeft = 1
	else: 
		checkTop = 0
		checkLeft = 0

	# checkTop = 1
	# checkLeft = 1

	path = [[0,0] for x in range(m+ 1)]
	path[index] = [j,j]


	#set boolean variables 

	#SET MAX VALUE
	curr = arr[i][j]

	if curr > maxLCS:
		maxLCS = curr

	# print "In backtrace, index of", index, "leads to j", j
	# print "outside while loop, this is path", path

	#recurse to backtrace
	while i>=0 and j >=0 and index >= 0: 

		#print "in the while loop, here are i,j,index values", i,j,index

		if i == 0 or j == 0 or index == 1:
			break

		curr = arr[i][j]
		diag = arr[i - 1][j - 1]
		left = arr[i][j-1]
		top = arr[i-1][j] 

		if checkTop == 0:
			#print "j is", j, "i is", index
			
			val =  p[l][index][1]
			#print val
			#print "compared to path[l][i-1][1]" p[l][i-1][1]
			if j <= val:
				#print "checktop should be true"
				checkTop = (j <= val)
			#print checkTop

		if checkLeft == 0:
			#print "CHECKLEFT"
			#print "j is", j, "i is", index
			
			val =  p[u][index][0]
			#print val
			checkLeft = (j >= p[u][index][0])
			#print checkLeft

		#first check top
		if curr == top and checkTop:
			path[index-1] = [j,j]
			index = index - 1
			i= i-1

		#next check left
		elif curr == left and checkLeft:
			path[index][0] = j-1
			j=j-1

		#finally check diagonal
		elif diag == curr-1:
			path[index-1] = [j-1,j-1]
			index = index - 1
			i = i - 1
			j = j - 1



		#reset boolean values
		if l != -1 and u != -1:
			checkTop = 0
			checkLeft = 0

	# print "the path we created is:"
	print path
	return path



def SingleShortestPath(A,B,mid,l,u):
	# print
	print "ENTERING SingleShortestPath"

	global p
	global arr


	m = len(A)/2
	n = len(B)
	A_str_curr = A[mid:mid+m]
	print "Strings we are comparing:", A_str_curr, B
	#this clears the row before
	arr[mid] = np.zeros(arraySize, dtype=int)
	for i in range(1,m +1):
		#print "at the beg of loop for i =", i
		#print "at the beginning of loop array is:"
		#print arr
		index = mid + i

		# print "at the beg of loop for index=", index
		# print "and u is:", u + 1
		# print "and l is:", l + 1

		# print "p of l"
		# print p[l]

		# print "p of u"
		# print p[u]


		leftBound = 1
		rightBound = n

		if index >= (u + 1):
			#print "index"
			leftBound = p[u][index - (u +1) + 1][0]
			#print "WE SOLVED FOR LEFTBOUND!"
			#print "left is", leftBound

		if index <= l + m:

			#print "index is:", index
			#print "left bound is", l+m
			#print "index-l+1 is.....", index-l
			rightBound = p[l][index-l][1]
			#print "WE SOLVED FOR RIGHTBOUND!"
			#print "index is", index
			#print "right is", rightBound

		# print 
		# print
		# print



		if leftBound== 0:
			print "LEFT WAS 0"
			leftBound = 1
		if rightBound== 0:
			print "RIGHT WAS 0"
		jrange = range(leftBound,rightBound + 1)

		
		# print "index is", index
		# if index <= u and index >= l:
		# 	jrange = range(1,plRight + 1)
		# 	print "CASE 1!!!!!!"
		# 	#print "1, plR"
		# elif index > u and index > l + m:
		# 	jrange = range(puLeft,n + 1)
		# 	print "CASE 2!!!!!!"
		# 	#print "puL, n"
		# elif index > u and index <= l + m:
		# 	jrange = range(puLeft,plRight +1)
		# 	print "CASE 3!!!!!!"
			#print "puL, puR"
		
		#print "jrange is", jrange
		for j in jrange:#range(1, n+1):  #jrange:#jrange:
			# print "j here is", j
			# print "A str:", A[index -1]
			# print "B str:", B[j-1]

			if A[index-1] == B[j-1]: # If we have a match 
				#print "WE MATCHED", A[index-1], B[j-1]
				arr[index][j] = arr[index-1][j-1]+1
			else:
				arr[index][j] = max(arr[index-1][j], arr[index][j-1])
		
	print arr[mid:mid + m + 1]
	#print
	#print
	#print "array when we do our method AT mid =", mid, A[mid], "l is:", l, A[l], "u is:", u, A[u]
	#print
	return PathBacktrace(A,B, mid, l, u)

# def FindShortestPath(A,B,p, l,u):
def FindShortestPath(A,B, l,u):
	print "FIND SHORTEST PATH IS CALLED with following values:"
	#print "A,B,l,u", A,B,l,u
	
	A_double = A + A
	if (u-l <= 1): 
		return
	mid = (l+u)/2 
	#print "the mid letter is", A[mid]

	p[mid] = SingleShortestPath(A_double,B,mid,l,u)
	#print "at the end of findshortestpath the path is the following:"
	#print p
	FindShortestPath(A,B,l,mid)
	FindShortestPath(A,B,mid,u)

def ComputeP0_Pm(A,B):
	global p
	#print "Strings we are comparing:", A, B
	p[0] = LCS(A,B)
	p[len(A)] = p[0]
	# print "total path after init"
	# print p

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
	# print "the total path array is:"
	# print p

	FindShortestPath(A,B,0,m)
	return maxLCS


def main():
	#print CLCSFast("ABGD", "ABCD")
	A = "ABCDE" 
	B = "CDKELEHSL"
	print "for strings:", A, B, "the answer is", CLCSFast(A, B)
	#print CLCSFast("C","CDCCCEDBDEADEACDEBAEDDEAEAADCAEDAD")
	#print CLCSFast("EBADAEEABBBCEDE", "ACBAAABDCAEADCEEBBDADDCEBCADCAEBBCDCAEDAC")
	#print CLCSFast("ACBBBCDCEDBADBBEABBEDAEADEBAEB", "AEBEEAEEABAEEBCACDBBAEABCEDCABEEDACEEC")


if __name__ == '__main__':
	main()




