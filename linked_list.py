#creating linked list
class node():
    def __init__(self,data,nextnode=None):
        self.data=data
        self.nextnode=nextnode
    def getdata(self):
        return self.data
    def setdata(self,val):
        self.data=val
    def getnextnode(self):
        return self.nextnode
    def setnextnode(self,val):
        self.nextnode=val
    def getnode(self):
        return self
        
        
class linkedlist():
    def createlist(self,data):
        p=node(data)
        self.head=p
    def insertnode(self,data):
        p=node(data)
        q=self.head
        while(q.getnextnode()!=None):
            q=q.getnextnode()
        q.setnextnode(p)
    def printlist2(self):
        q = self.head
        while q:
            print(q.data)
            q = q.getnextnode()
    def printlist(self):
        q=self.head
        while(q.getnextnode()!=None):
            print(q.getdata())
            q=q.getnextnode()
