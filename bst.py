def bst(root,value):
    if root==None:
        return Node(value)
    elif root.data>value:
        root.left=bst(root.left,value)
    else:
        root.right=bst(root.right,value)
    return root