# print question
# accept user answer
# tell user if they got it right

print("\nWelcome to the quiz!\n")

q_text = """What according to the story, 
fell on Newton's head to inspire 
him to discover gravity?\n"""

ans_a = "(a) An apple"
ans_b = "(b) A banana"
ans_c = "(c) A can of beans"
ans_d = "(d) A donut"

ans_list = [ans_a, ans_b, ans_c, ans_d] 

print(q_text)
for item in ans_list:
    print(item)

user_ans = input("Give your answer (a, b, c or d):\n> ")
print(f"You answered: {user_ans}")
if user_ans == "a":
    print("You were right :)")
else:
    print("You were wrong :(")