# ask 3 questions and tell user how many they have answered correctly
# validate the user input
# tell the user the correct answer

q1_text = """What according to the story, 
fell on Newton's head to inspire 
him to discover gravity?\n"""

ans1_a = "(a) An apple"
ans1_b = "(b) A banana"
ans1_c = "(c) A can of beans"
ans1_d = "(d) A donut"

correct1 = "a"

q2_text = """What was one unusual thing about Mr Spock?\n"""

ans2_a = "(a) He has blue skin"
ans2_b = "(b) He had a ridged forehead"
ans2_c = "(c) He can shapeshift"
ans2_d = "(d) He has pointed ears"

correct2 = "d"


q3_text = """Who is Barbie's boyfriend?\n"""

ans3_a = "(a) Benji"
ans3_b = "(b) Lenny"
ans3_c = "(c) Ken"
ans3_d = "(d) Dennis"

correct3 = "c"

ans1_list = [ans1_a, ans1_b, ans1_c, ans1_d] 
ans2_list = [ans2_a, ans2_b, ans2_c, ans2_d] 
ans3_list = [ans3_a, ans3_b, ans3_c, ans3_d]

num_q_correct = 0

print("\nWelcome to the quiz!\n")

print(q1_text)
for item in ans1_list:
    print(item)

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
if user_ans == correct1:
    print("You were right :)")
    num_q_correct += 1
else:
    print("You were wrong :(")
    print(f"The correct answer was ({correct1})")

print(q2_text)
for item in ans2_list:
    print(item)

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
if user_ans == correct2:
    print("You were right :)")
    num_q_correct += 1
else:
    print("You were wrong :(")
    print(f"The correct answer was ({correct2})")
    
print(q3_text)
for item in ans3_list:
    print(item)

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
if user_ans == correct3:
    print("You were right :)")
    num_q_correct += 1
else:
    print("You were wrong :(")
    print(f"The correct answer was ({correct3})")
    
print("\n\nEnd of the quiz!!!")
print(f"You got {num_q_correct}/3")