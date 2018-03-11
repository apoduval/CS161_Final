#CLCSSlow Implementation

# Compute shortest path of mid (pm) using dynamic programming bounded by pl and pu
def SingleShortestPath(A,B,m,pl,pu)


def FindShortestPath(A,B,p,l,u):
     if (u-l <= 1) return
     mid = (l+u)/2
     p[mid] = SingleShortestPath(A,B,mid,p[l],p[u])
     FindShortestPath(A,B,p,l,mid)
     FindShortestPath(A,B,p,mid,u)
     


def CLCSSlow(A,B):

	m = len(A)
	n = len(B)
    p = []# array of arrays to represent paths?
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