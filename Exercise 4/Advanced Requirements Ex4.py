#Question of countries and their capitals
questions = {
    "France": "Paris",
    "Belgium": "Brussels",
    "Portugal": "Lisbon",
    "Ireland": "Dublin",
    "Germany": "Berlin",
    "Netherlands": "Amsterdam",
    "Switzerland": "Bern",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London"
}

#To ask the user 10 question about european countries and their capitals
for country, correct_capital in questions.items():
    ans = input(f"What is the capital of {country}? ").strip().lower()
        
    # To check if the answer is correct or incorrect
    if ans == correct_capital.lower():
        print("Correct Answer.")
    else:
        print(f"Incorrect Answer. The correct answer is {correct_capital}.")

    