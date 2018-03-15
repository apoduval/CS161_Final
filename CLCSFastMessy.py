#CLCSFast
import sys
import numpy as np

arraySize = 30
arr = np.zeros((2*arraySize,arraySize), dtype=int)

p = [[[]]]

maxLCS = -1

#important note, we would only need mid,l,u if we wanted to compare to path
def PathBacktrace(A,B, mid, l, u, jrange_arr):
	global maxLCS
	print "enter backtrace"
	#print "l", A[l], "u", u


	m = len(A)/2
	index = m 


	print "string A", A[mid:mid+m], "string B", B
	print "the array is"	
	print arr[mid:mid + m + 1]



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
		print maxLCS

	# print "In backtrace, index of", index, "leads to j", j
	# print "outside while loop, this is path", path
#	print "out the while loop, here are i,j, index,  values", i, j, index
	#recurse to backtrace
	while i>=0 and j >=0 and index >= 0: 

		if i == 0 or j == 0 or index == 1:
			break

		curr = arr[i][j]

		diag = arr[i - 1][j - 1]
		left = arr[i][j-1]
		top = arr[i-1][j] 

		#print "in the while loop, here are i,j, index", i,j,index
		#print "and here are the values curr diag left top", curr, diag, left, top
		# print "pl is", p[l]
		# print "pu is", p[u]
		if checkTop == 0:

			#-------------------------------------------OLD METHOD
			#print "i-1", i-1, "l+m,", l+m

			# if i - 1 <= l + m:
			# 	#if i > m: 
			# 		#tempIndex = 
			# 	#print "i - l + 1", i-l+ 1
			# 	x = p[l][i-(l+ 1)][1]
			# 	#print "j is", j, "val is", right

			# #print "compared to path[l][i-1][1]" p[l][i-1][1]
			# 	if j <= x:
			# 		#print "checktop should be true"
			# 		checkTop = 1
			# else: 
			# 	checkTop = 1
			# #print checkTop
			# 		#print checkTop

			#-------------------------------------------OLD METHOD
	#		print "new top check comparing j", j, "with", jrange_arr[index-1]
			if j >= jrange_arr[index-1][0] and j <= jrange_arr[index-1][1]:
		#		print "checkTop is now true!"
				checkTop = 1


		#print "checktop is", checkTop
		#print "AFTER THE FACT---------------"
		
		if checkLeft == 0:
			#-------------------------------------------OLD METHOD
			#print "CHECKLEFT"
			#print "j is", j, "i is", index
			# if i >= u:
			# 	# print "i >= u"
			# 	# print "p[u] is", p[u]
			# 	y = p[u][(mid + index)-u][0]
			# 	# print "calculation", (mid + index)-u
			# 	# print "y is", y
			# 	# print "u is", u
			# 	# print "mid is,", mid
			# 	# print "i is", i
			# 	# print "j-1 is", j-1
			# 	if j-1>= y:
			# 		checkLeft = 1 

			# else: 
			# 	checkLeft = 1

			#-------------------------------------------OLD METHOD
		#	print "new left check comparing j-1", j-1, "with", jrange_arr[index]
			if j - 1 >= jrange_arr[index][0]:
			#	print "checkleft is now true!"
				checkLeft = 1

			# val =  p[u][index][0]
			# #print val
			# checkLeft = (j >= p[u][index][0])
			#print checkLeft

	#	print "here are the possible points:"
		#print "curr", curr, "diag", diag, "left", left, "top", top
		
		bl = 0
		if curr == top:
			bl = 1

	#	print "curr == top", bl
		#print "checkTop ", checkTop
		#first check top
		if (curr == top and checkTop) or (checkLeft != 0 and diag != curr - 1):
		#	print "went up"
			path[index-1] = [j,j]
			index = index - 1
			i= i-1

		#next check left


		elif (curr == left and checkLeft) or  (checkTop != 0 and diag != curr - 1):
		#	print "---------------------went left"
			path[index][0] = j-1
			j=j-1
			#print "after, j value is", j

		#finally check diagonal
		elif diag == curr-1:
			#print "went diag"
			path[index-1] = [j-1,j-1]
			index = index - 1
			i = i - 1
			j = j - 1



		#reset boolean values
		if l != -1 and u != -1:
			checkTop = 0
			checkLeft = 0


		#print "at bottom of loop j", j
	# 	print "path is every iteration is"
	# 	print path
	# 	print 
	# 	print 
		

	# print "the path we created is end of while loop:"
	#print path
	return path


def SingleShortestPath(A,B,mid,l,u):
	# print
	print "ENTERING SingleShortestPath"

	global p
	global arr


	m = len(A)/2
	n = len(B)
	A_str_curr = A[mid:mid+m]
#	print "Strings we are comparing:", A_str_curr, B
	#this clears the row before
	arr[mid] = np.zeros(arraySize, dtype=int)


	jrange_arr = [[0,0] for i in range(m + 1)]
	jrange_arr[0] = [0,n]
#	print "initial jrange arr--------------------------------", jrange_arr

	for i in range(1,m +1):
		#print "ENTERING FOR LOOP FOR i", i
		#print "at the beg of loop for i =", i
		#print "at the beginning of loop array is:"
		#print arr
		index = mid + i

		# print "at the beg of loop for index=", index
		# print "and u is:", u + 1
		# print "and l is:", l + 1

		print "p of l"
		print p[l], "for l", l

		print "p of u"
		print p[u], "for u", u


		leftBound = 1
		rightBound = n

		if index >= u+1:
			# print "index", index
			# print "left bound is", u+1
			# print "WE SOLVED FOR LEFTBOUND!"
			# print "index - (u +1),", index - (u)
			leftBound = p[u][(index - u )][1]
			# print "left is", leftBound

		if index <= l + m:
			# print "WE SOLVED FOR RIGHTBOUND!"
			# print "index is:", index
			# print "left bound is", l+m
			# print "index-l+1 is.....", index-l
			rightBound = p[l][index-l][0]
			#print "index is", index
			# print "right is", rightBound

		# print 
		# print
		# print



		if leftBound== 0:
			#print "LEFT WAS 0"
			leftBound = 1
		if rightBound== 0:
			#print "RIGHT WAS 0"
			rightBound = 1
		jrange = range(leftBound,rightBound + 1)
		jarr = [leftBound, rightBound]
		#print "jrange is------------------------------------------", jarr
		jrange_arr[i] = [leftBound, rightBound]
		# print "at index i,", i
		print "jrange is------------------------------------------", jrange_arr 
		# print
		# print
		#print "testing jrange_arr", jrange_arr, "for i", i
		
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
		



		#print "pl", p[l]
		#print "pu", p[u]

		#seekingmatch = 1

		for j in jrange:#range(1, n+1):  #jrange:#jrange:
			#print "j is", j

			#print "j here is", j
			# print "A str:", A[index -1]
			# print "B str:", B[j-1]

			if A[index-1] == B[j-1]: #and seekingmatch: # If we have a match 
				print "we match", A[index-1], B[j-1], i, j 
				if j-1 >= jrange_arr[i-1][0] and j-1 <= jrange_arr[i-1][1]:
				#print "testing jrange_arr bounds for MATCH in bounds", j-1, "vs.", jrange_arr[i-1][0], jrange_arr[i-1][1]
				#	print "i set index j to ", arr[index-1][j-1] + 1
					arr[index][j] = arr[index-1][j-1]+1
				else:
				#	print "testing jrange_arr bounds for MATCH out of bounds", j-1, "vs.", jrange_arr[i-1][0], jrange_arr[i-1][1]
				#	print "i set index j to ", arr[index][j-1] + 1
					arr[index][j] = arr[index][j-1] + 1
				seekingmatch = 0

			else:
				print "no match", A[index-1], B[j-1], i, j 

				if j >= jrange_arr[i-1][0] and j <= jrange_arr[i-1][1]:
					#print "testing jrange_arr bounds for NO match in bounds", j, "vs.", jrange_arr[i-1][0], jrange_arr[i-1][1]
					#print "i set index j to ", max(arr[index-1][j], arr[index][j-1])
					arr[index][j] = max(arr[index-1][j], arr[index][j-1])
				else:
					#print "testing jrange_arr bounds for NO match out of bounds", j, "vs.", jrange_arr[i-1][0], jrange_arr[i-1][1]
					#print "i set index j to ", arr[index][j-1]
					arr[index][j] = arr[index][j-1]
		
	#	print
	#	print

	#print
	#print "end of for loop for i = ", i

	#print
	#print
	#print "array when we do our method AT mid =", mid, A[mid], "l is:", l, A[l], "u is:", u, A[u]
	#print
	#print "before backtrace, this is path", p
	return PathBacktrace(A,B, mid, l, u, jrange_arr)

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
	#print arr

	return PathBacktrace(A + A,B, 0, -1, -1, 0)

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
	A = "ABCD" 
	B = "ABCDE"
	print "for strings:", A, B, "the answer is", CLCSFast(A, B)
	#print CLCSFast("C","CDCCCEDBDEADEACDEBAEDDEAEAADCAEDAD")
	#print CLCSFast("EBADAEEABBBCEDE", "ACBAAABDCAEADCEEBBDADDCEBCADCAEBBCDCAEDAC")
	#print CLCSFast("ACBBBCDCEDBADBBEABBEDAEADEBAEB", "AEBEEAEEABAEEBCACDBBAEABCEDCABEEDACEEC")


if __name__ == '__main__':
	main()




