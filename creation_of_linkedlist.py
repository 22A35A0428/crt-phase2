class node:
    def __init__(self,data):
        self.data=data
        self.next=None


ele1=node(71)
ele2=node(72)
ele3=node(73)
ele4=node(74)
ele5=node(75)


ele1.next=ele2
ele2.next=ele3
ele3.next=ele4
ele4.next=ele5


a=ele1
while a!=None:
    print(a.data,end='^^^^')
    a=a.next

