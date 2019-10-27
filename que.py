#que using array
class que():
    l=[]
    length=0
    c=0
    
    def push(self,n):
        if(self.length>=self.c):
            self.l.append(n)
            self.c=self.c+1
        else:
            print("the que is full")
    
    def pop(self):
        if(len(self.l)!=0):
            del(self.l[0])
            self.c=self.c-1
        else:
            print("the que is empty")
    
    def display(self):
        print(self.l)
