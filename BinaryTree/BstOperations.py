def insert_node(root, node):
	if root==None:
		root=node

	if root.data > node.data:
		if root.lchild==None:
			root.lchild=node
		else:
			insert_node(root.lchild, node)
	else:
		if root.rchild==None:
			root.rchild=node
		else:
			insert_node(root.rchild,node)


