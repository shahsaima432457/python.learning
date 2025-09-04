
# continue :terminates execution in the current iteration and continues execution of the loop  with the next iteration

# continue acts as skip
i = 0 
while i <= 14:
    if(i == 10):
        i += 1
        continue
    print(i)
    i += 1
    
#  wap  using while loop  continue statements
#print oddnumber and skip odd numbers

i = 1
while i <= 14:
    if(i % 2 == 0):
        i += 1
    # print(i)
        continue
    print(i)
    i += 1
    
#  wap  using while loop  continue statements
#print  odd  numbers and skip odd numbers

# m = 1

# while m <= 7:
#     if ( m % 2 !=  0):
#         m += 1
#     # print(i)
#         continue
#     print(m)


i = 1
while i <= 14:
    if(i % 2 != 0):
        i += 1
    # print(i)
        continue
    print(i)
    i += 1
    
