# Methods vs Functions
'''
  The methods arre the functions written inside of class.
  
  l=[1,2,3]
  x=len(l) # len() is the function which is acessed by any object
  
  l.append() # append is the method which is acessed only by object of
                perticular class not by any object 
  
'''


class ATM:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        user_input='''
        HEllo, how would you like to proceed
        1. Enter 1 to create pin
        2. Enter 2 to deposite
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        '''
        if user_input=='1':
            print("Create Pin")
        elif user_input=='2':
            print('Deposite Amount')
        elif user_input=='3':
            print('Withdraw')
        elif user_input=='4':
            print('Check Balance')
        elif user_input=='5':
            print('Bye')