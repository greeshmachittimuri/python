class Reverse:
   def rev_num(self,n):
      rev=0
      while n>0:
         i=n%10
         rev=rev*10+i
         n=n//10
      print(f'reverse of a number {x} is {rev}')

n=int(input('enter the number:')) 
x=n
ob=Reverse()
ob.rev_num(n)
