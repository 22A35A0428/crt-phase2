class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printing(head):
    cn=head
    while cn!=None:
        print(cn.data,end='++')
        cn=cn.next
    print()

#headdddddd
def athead(head,e):
    temp=node(e)
    temp.next=head
    return temp

#tailllll
def linking(head,ele):

    temp=node(ele)
    if head==None:
        return temp
    
    tail=head
    while tail.next !=None:
        tail=tail.next    
    tail.next=temp
    return head

def pos(head,postion,ele):
    if postion==0:
        return athead(head,ele)
    
    i=0
    temp=node(ele)
    cn=head
    while i!=postion-1:
        cn=cn.next
        i+=1
    nextele=cn.next
    cn.next=temp
    temp.next=nextele
    return head




num=[11,22,29,35,22,45,765]
head=None
for i in num:
    head=athead(head,i)
head=pos(head,2,222)
printing(head)






        