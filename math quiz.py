import random
import time

# generator two random numbers
def question_generator():
    # generate two random numbers
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    # random operator
    operator_list = ["+", "-", "*"]
    selected_operator = random.choice(operator_list)
    print(f"{a} {selected_operator} {b} = ?")
    
    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a * b

question_number_limit = 5
question_number = 0
score = 0
time_limit = 10

while question_number < question_number_limit:
    # step 1: generate a random question (DONE!)
    result = str(question_generator())
    start_time = time.time()

    # step 2: get user answer (DONE!)
    user_answer = input("Enter your answer: ")
    end_time = time.time()
    time_dif = end_time - start_time

    # step 3: check the answer and time
    if time_dif < time_limit:
        if result == user_answer:
            score += 1
            print(f"Perfect, score: {score}")
        else:
            print("Sorry! Your answer is wrong.")
    else:
        print(f"You are too late!")

    question_number += 1

print(f"Final score: {score} out of {question_number_limit}")
