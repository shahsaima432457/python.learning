# range function returns a sequence of numbers, strarting from o  by default, 
#and increments by 1 by default and stops before a specified number

# #rangestart,stop,step

# print(range(10))


# # shows the range means start to end
# # another method
# seq = range (5)

# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[0])


seq = range (13)
for i in seq:
    print(i)
    

# there are three types of writing range

for i in range(10):#range (stop)
    print(i)
    



for i in range(10,20):
#range (start,stop)
    print(i)
    



for i in range(10,20,4):
#range (start,stop,step)
    print(i)
    

# print odd number

for i in range(1,100,1):
    print(i)
    

# print even number

for i in range (1,10,2):
    print(i)
    


# print numbers from 1 to 100

for i in range (1,101):
    print(i)
    

# print numbers from  100 to 1

for i in range (100,0,-1):
    print(i)
    


# multiplication of number n


n =int (input("enter the number"))

for i in range (1,11):
    print(i*n)
                    


