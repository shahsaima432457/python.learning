# i can create a program for makeup
skincare ={
        "lip care" :49,
        "mascara":12,
        "skincare":200,
        "body lotion":234,
        "hand wash":100,
}
print(skincare)
print("welcome to  my world")
print("lip care: Rs 49\n mascara : RS 12\n sm : RS 200\n body lotion : RS 234\n")

total_products = 0
product1 =input("enter the first order")

if  product1 in skincare:
    total_products +=skincare[product1]
    print("your item has been added to your order list")
    
else:
    print("sorry this item is not availabe  right now , try to add any other one")


product2 =input("Do you want to add any item in car  Yes/No")


if product2 == "yes":
    product3 = input("enter the second product ")
    if product3 in skincare:
        total_products +=skincare[product3]
        print("added to your card")
    else:
        print("this product is not in the availabe right now right another one")
            
        print("thankyou so much for visiting my app")
        
print(f"the total amount of item to pay is {total_products}")