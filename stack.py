class Stack:
    def __init__(self,size):
        self.stack=['none']*size
        self.top=-1
        self.size=size
    def is_full(self):
        return self.top==self.size-1
    def is_empty(self):
        return self.top==-1
         
    def push(self,data):
        if self.is_full():
            print('stack is full')
        else:
            self.top+=1
            self.stack[self.top]=data
            print(self.stack)
    def pop(self):
        if self.is_empty():
            print('stack is empty')
        else:
            temp=self.stack[self.top]
            self.stack[self.top]='none'  
            self.top-=1
            print(self.stack)
            print(temp)
    def  display(self):
        if(self.is_empty()):
            print('stack is empty')
        else:
            #self.top+=1
            for i in range(self.top,-1,-1):
                print(self.stack[i])
size=int(input('enter the size of the stack:'))                  
ob=Stack(size)
while True:
    print('1 for inserting')
    print('2 for display')
    print('3 for deleting')
    ch=int(input('enter the  your choice:'))  
    if(ch==1): 
        data=int(input('enter the data to insert:'))
        ob.push(data) 
    elif(ch==2):
        ob.display()
    elif(ch==3):
        ob.pop()
        break

    else:
        
        print('invalid choice')

