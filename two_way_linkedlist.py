#crating a two way linkedlist
class node():
    def __init__(self,data,nextnode=None,prevnode=None):
        self.data=data
        self.nextnode=nextnode
        self.prevnode=prevnode
    def getdata(self):
        return self.data
    def setdata(self,val):
        self.data=val
    def getnextnode(self):
        return self.nextnode
    def setnextnode(self,val):
        self.nextnode=val
    def getprevnode(self):
        return self.prevnode
    def setprevnode(self,val):
        self.prevnode=val
    def getnode(self):
        return self
    
class twoway_linkedlist():
    def __init__(self,head=None,length=0):
        self.head=head
        self.length=length
    def create(self,val):
        p=node(val)
        self.head=p
        self.length=1
    def insert(self,pos,val):
        p=node(val)
        q=self.head
        if(pos>self.length+1):
            print("not possible")
        else:
            n=self.length
            if(pos==1):
                p.setnextnode(self.head)
                self.head.setprevnode(p)
                self.head=p
            elif(pos==self.length+1):
                for i in range(1,n,1):
                    q=q.getnextnode()
                q.setnextnode(p)
                p.setprevnode(q)
            else:
                for i in range(1,n,1):
                    q=q.getnextnode()
                p.setprevnode(q)
                p.setnextnode(q.getnextnode())
                q.getnextnode().setprevnode(p)
                q.setnextnode(p)
            self.length=self.length+1
    def printlist(self):
            q=self.head
            for i in range(1,self.length+1,1):
                print(q.getdata())
                q=q.getnextnode()
