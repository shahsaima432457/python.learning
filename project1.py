# Simple Quiz Game in Python

# Step 1: Store questions and answers
quiz = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who developed Python Programming Language?": "Guido van Rossum",
    "What is the square root of 81?": "9"
}

# Step 2: Initialize score
score = 0

# Step 3: Loop through the quiz questions
for question, answer in quiz.items():
    print("\n" + question)  # show question
    user_answer = input("Your answer: ")  # take input
    
    # Step 4: Check the answer
    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {answer}")

# Step 5: Show final score
print("\n🎯 Quiz Completed!")
print(f"Your final score is {score}/{len(quiz)}")
