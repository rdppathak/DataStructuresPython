def get_sum (BiTree, i):
	s = 0
	i = i+1
	while i>0:
		s += BiTree[i]
		i -= i & (-i)

	return s

def update_bit(BitTree, n, i, v):
	i += 1
	
	while i<=n:
		BitTree[i] +=v
		i += i & (-i)


def contruct_tree(arr, n):
	BitTree = []

	BitTree = [0]*(n+1)

	for i in xrange(n):
		update_bit(BitTree, n, i, arr[i])

	return BitTree

def main():
	arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
	BitTree = contruct_tree(arr, len(arr))

	print BitTree

	print "Sum of first %s elements: %s"%(0, get_sum(BitTree, 0))

if __name__ == '__main__':
	main()

