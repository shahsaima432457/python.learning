game={
    "which is your favourite langueage":"python",
    "which is your favourite color":"pink",
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
   "Who developed Python Programming Language?": "Guido van Rossum",
    "What is the square root of 81?": "9"
    }
score = 0
for question, answer  in game.items():
    print(question)  
    a = input("enter the number")
    
    if a.strip().lower() ==  answer.lower():
        print("answer")
        score += 1
    else:
        print("not correct answer")
        
print("quiz completed")
    
    
    
