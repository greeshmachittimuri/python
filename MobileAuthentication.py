from abc import ABC,abstractmethod
class Authentication(ABC):
    @abstractmethod
    # def __init__(self,username,userpassword,userotp):
    #     self.username=username
    #     self.userpassword=userpassword
    #     self.userotp=userotp
    def login(self):
        pass
class Password(Authentication):
    def __init__(self,username,userpassword):
        self.username=username
        self.userpassword=userpassword
    def login(self):
        name='greeshma'
        password="12gr"
        if(password==userpassword and name==username):
            print('loggged in succesufully')
        else:
            print('invalid password')
class Otp(Authentication):
    def __init__(self,userotp): 
        self.userotp=userotp
    def login(self):
        otp=1234
        if (otp==userotp):
            print('succesfully logged')
        else:
            print('invalid')
class FringerPrint(Authentication):
     def __init__(self,uservalue): 
        self.uservalue=uservalue
     def login(self):
        value=9087
        name='greeshma'
        if(value==uservalue and name==username):
            print("succesfully logged")
        else:
             print('invalid')

ch=int(input('enter the choice:'))
if(ch==1):
       username=input('enter the name:')
       userpassword=input('enter password:')  
       ob=Password(username,userpassword)
    
elif(ch==2):
       
       userotp=input('enter the otp:')
       ob=Otp(userotp)
elif(ch==3):
      username=input('enter the name:')
      uservalue=eval(input('enter the your value:'))
      ob=FringerPrint(uservalue)

    
ob.login()    