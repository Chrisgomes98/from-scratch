#creating stack using array
class stack():
    l=[]
    length=0
    c=0
    def push(self,n):
        if(self.c<self.length):
            self.l.append(n)
            self.c=self.c+1
        else:
            print("the stack is full")
    def display(self):
        print(self.l)
    def pop(self):
        del(self.l[self.c-1])
        self.c=self.c-1
