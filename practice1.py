#search for a number x in this tuple using loop

num = (1,4,9,16,25)

i = 0
while i < len(num):
    
    print(num[i])
    i +=1
#search for a number x in this tuple using loop and find the x

num = (1,4,9,16,25)
x =9
i = 0
while i < len(num):
    
    if(num[i] == x):
        print("found item",i)
    else:
        print("finding................")
    
    print(num[i])
    i +=1

