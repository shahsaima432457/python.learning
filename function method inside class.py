class Design:   
    # Class variable
    a = 10
    
    # Function (method) inside class
    def value(self):
        print(20 + 30)   # prints 50

    def sum(self):
        print(200 - 220) # prints -20

# create an object of class
demo = Design()

# Access class variable
print(demo.a)   # Output: 10

# Call functions using object
demo.value()    # Output: 50
demo.sum()      # Output: -20
