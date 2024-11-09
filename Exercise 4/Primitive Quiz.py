# To ask the user a question 
qns= input("What is the capital of France? ").strip().lower()

# To check the answer if its true or not
if qns == "paris":
    print("The answer is Correct.")
else:
    print("The answer is Incorrect. The Correct answer is Paris.")
