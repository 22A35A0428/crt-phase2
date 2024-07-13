class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def insertbst(root,val):
    if root==None:
        return node(val)
    elif root.data>val:
        root.left=insertbst(root.left,val)
    else:
        root.right=insertbst(root.right,val)
    return root




num=[45,21,35,11,95,22,11,29]
root=None
for k in num:
    root=insertbst(root,k)
print(k)