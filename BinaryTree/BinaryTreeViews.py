import Queue
class Node:
	def __init__(self, data, lchild=None, rchild=None):
		self.data = data
		self.lchild = lchild
		self.rchild = rchild

def bottom_view(root, level):
	if root == None:
		return

	q = Queue.Queue()

	q.put((root, level))

	view_map = {}

	while (not q.empty()):
		node, sub_level = q.get()

		view_map[sub_level] = node.data
		if node.lchild != None:
			q.put((node.lchild, sub_level-1))
		if node.rchild != None:
			q.put((node.rchild, sub_level+1))

	keys = view_map.keys()
	keys.sort()
	for key in keys:
		print view_map[key]," ",

def top_view(root, level):
	if root == None:
		return

	q = Queue.Queue()

	q.put((root, level))

	view_map = {}

	while (not q.empty()):
		node, sub_level = q.get()

		if not view_map.has_key(sub_level):
			view_map[sub_level] = node.data

		if node.lchild != None:
			q.put((node.lchild, sub_level-1))
		if node.rchild != None:
			q.put((node.rchild, sub_level+1))


	keys = view_map.keys()
	keys.sort()

	for key in keys:
		print view_map[key]," ",

llevel=0
def left_view(root, current_level):
	global llevel
	if root == None:
		return

	if current_level > llevel:
		print root.data, " ",
		llevel=llevel+1

	if root.lchild != None:
		left_view(root.lchild, current_level+1)
	if root.rchild != None:
		left_view(root.rchild, current_level+1)

rlevel = 0
def right_view(root, current_level):
	global rlevel
	if root == None:
		return

	if current_level > rlevel:
		print root.data, " ",
		rlevel=rlevel+1

	if root.rchild != None:
		right_view(root.rchild, current_level+1)
	if root.lchild != None:
		right_view(root.lchild, current_level+1)

def main():
	root = Node(20)
	root.lchild = Node(8)
	root.rchild = Node(22)
	root.lchild.lchild = Node(5)
	root.lchild.rchild = Node(3)
	root.lchild.rchild.lchild = Node(10)
	root.lchild.rchild.rchild = Node(14)
	root.rchild.rchild = Node(25)

	print "Bottom View of tree "
	bottom_view(root, 0)
	print ""

	print "Top View of tree "
	top_view(root, 0)
	print ""

	global level
	level = 0
	print "Left view of tree is as follows:"
	left_view(root, 1)
	print ""

	global rlevel
	rlevel = 0
	print "Right view of tree is as follows:"
	right_view(root, 1)
	print ""

if __name__ == '__main__':
	main()