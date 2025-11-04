# use dictionary structure to store question parts
# store set of questions in a list
# keep track of money and end if user gets question wrong

q1_dict = {
    "q": """What according to the story, 
fell on Newton's head to inspire 
him to discover gravity?\n""",
    "a": "an apple",
    "b": "a banana",
    "c": "a can of beans",
    "d": "a donut",
    "correct": "a"
}


q2_dict = {
    "q": """What was one unusual thing about Mr Spock?\n""",
    "a": "he has blue skin",
    "b": "he had a ridged forehead",
    "c": "he can shapeshift",
    "d": "he has pointed ears",
    "correct": "d"
}

q3_dict = {
    "q": """Who is Barbie's boyfriend?\n""",
    "a": "Benji",
    "b": "Lenny",
    "c": "Ken",
    "d": "Dennis",
    "correct": "c"
}

q_list = [q1_dict, q2_dict, q3_dict]

ans_keys = ["a", "b", "c", "d"]

stage = 0

levels = [0, 100, 250, 500, 1000, 2000]

print("\nWelcome to the quiz!\n")
for q_dict in q_list:

    print(f"You are playing for: £{levels[stage + 1]}")

    print(q_dict["q"])
    for k in ans_keys:
        print(f"({k}) {q_dict[k]}")

    user_ans = input("Give your answer (a, b, c or d):\n> ")
    # sanitise user input
    user_ans = user_ans.lower()
    user_ans = user_ans.strip()

    # validate and loop until valid input given
    while user_ans not in ["a","b","c","d"]:
        print("Sorry that was not an option.")
        user_ans = input("Try again:\n> ")
        # sanitise user input
        user_ans = user_ans.lower()
        user_ans = user_ans.strip()

    print(f"You answered: {user_ans}")
    if user_ans == q_dict["correct"]:
        print("You were right :)")
        stage += 1
    else:
        print("You were wrong :(")
        correct_key = q_dict["correct"]
        print(f"The correct answer was {q_dict[correct_key]}.")
        break

print(f"Game Over... You won £{levels[stage]}")