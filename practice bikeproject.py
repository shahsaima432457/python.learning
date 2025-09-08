# display available bikes
# request a bike for rent1=100
#exit
# create a class
class Bike:
    # create constructor
    def __init__(self,stock):
        self.stock = stock
        
    def Display(self):
        print("Total stock of bike ", self.stock)
        
    def rent(q):
        if q <= 0:
            print("please select a value greater than one :")
    # obj = Bike(100)
        elif q > self.stock:
            print("Please select a value less than or equal to stock value.")
        else:
            print("Total price:", q * 100)
            self.stock -= q
            print("Bikes left:", self.stock)
    
    while True:
        uc=int(input('''
            1. Display stock
            2. Rent a Bike
            3. Exit
            Enter your choice:
                        '''))
    
if uc == 1:
    obj.display()
elif uc ==2:
    # rent a bike
    # first we need to know  the customer quantity
    n=input("enter the  quantity of bike:")
    obj.rent(n)
    
elif uc == 3:
    print("thank you for visiting. Goodbye")
    
else:
    print("Invalid choice, please try again")
        
            
