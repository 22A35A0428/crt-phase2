class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def pre(root,l1):
    if root==None:
        return
    l1.append(root.data)
    pre(root.left,l1)
    pre(root.right,l1)


def inor(root,l2):
    if root==None:
        return
    inor(root.left,l2)
    l2.append(root.data)
    inor(root.right,l2)

def post(root,l3):
    if root==None:
        return
    post(root.left,l3)
    post(root.right,l3)
    l3.append(root.data)
    

obj1=node(1)
obj2=node(11)
obj3=node(22)
obj4=node(29)
obj5=node(30)
obj6=node(31)
obj7=node(35)

obj1.right=obj3
obj1.left=obj2
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7

l1=[]
l2=[]
l3=[]
pre(obj1,l1)
inor(obj1,l2)
post(obj1,l3)

print(l1)
print(l2)
print(l3)
