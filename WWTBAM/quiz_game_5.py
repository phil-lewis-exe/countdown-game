# Loop game to allow more than one player to play
# Record player name and scores
# Ask user if it is their final answer (y/n)
# Include 50:50 (remove two wrong answer) 3 times during game

import random
from time import sleep

def play_game():
    n_questions = 14

    stage = 0

    levels = [0, 100, 250, 500, 1000, 2000, 4000, 8000, 
          16_000, 32_000, 64_000, 125_000, 250_000,
          500_000, 1_000_000]

    print("\nWelcome to the quiz!\n")
    result = True
    while stage < 14 and result == True:

        q_dict = q_list[stage]
        print(f"You are playing for: £{levels[stage + 1]}")

        result = ask_question(q_dict)
        
        if result == True:
            stage += 1
        sleep(3)
    print(f"Game Over... You won £{levels[stage]}")
    return levels[stage]

def ask_question(q_dict):
    ans_keys = ["a", "b", "c", "d"]
    print(q_dict["q"])
    for k in ans_keys:
        print(f"({k}) {q_dict[k]}")
    
    final_ans = False
    while final_ans == False:
        user_ans = get_user_input( ans_keys )
        check = input("Final answer? (y/n): ")
        if check == "y":
            final_ans = True

    print(f"You answered: {user_ans}")
    sleep(3)
    if user_ans == q_dict["correct"]:
        print("You were right :)")
        return True
    else:
        print("You were wrong :(")
        correct_key = q_dict["correct"]
        print(f"The correct answer was {q_dict[correct_key]}.")
        return False

def get_user_input(char_list):
    user_ans = input("Give your answer (a, b, c or d):\n> ")
    # sanitise user input
    user_ans = user_ans.lower()
    user_ans = user_ans.strip()

    # validate and loop until valid input given
    while user_ans not in char_list:
        print("Sorry that was not an option.")
        user_ans = input("Try again:\n> ")
        # sanitise user input
        user_ans = user_ans.lower()
        user_ans = user_ans.strip()
    return user_ans

q_list = [
    {
        "q": "What color do you get when you mix red and white?",
        "a": "Pink",
        "b": "Purple",
        "c": "Orange",
        "d": "Brown",
        "correct": "a"
    },
    {
        "q": "How many legs does a spider have?",
        "a": "6",
        "b": "8",
        "c": "10",
        "d": "12",
        "correct": "b"
    },
    {
        "q": "What is the capital city of France?",
        "a": "Rome",
        "b": "Paris",
        "c": "Madrid",
        "d": "Berlin",
        "correct": "b"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "a": "Mars",
        "b": "Venus",
        "c": "Jupiter",
        "d": "Saturn",
        "correct": "a"
    },
    {
        "q": "Who wrote the play 'Romeo and Juliet'?",
        "a": "Charles Dickens",
        "b": "William Shakespeare",
        "c": "Mark Twain",
        "d": "Jane Austen",
        "correct": "b"
    },
    {
        "q": "Which ocean is the largest?",
        "a": "Atlantic Ocean",
        "b": "Pacific Ocean",
        "c": "Indian Ocean",
        "d": "Arctic Ocean",
        "correct": "b"
    },
    {
        "q": "What is the hardest natural substance on Earth?",
        "a": "Gold",
        "b": "Iron",
        "c": "Diamond",
        "d": "Platinum",
        "correct": "c"
    },
    {
        "q": "Which gas do plants absorb during photosynthesis?",
        "a": "Oxygen",
        "b": "Hydrogen",
        "c": "Carbon Dioxide",
        "d": "Nitrogen",
        "correct": "c"
    },
    {
        "q": "Who painted the 'Mona Lisa'?",
        "a": "Michelangelo",
        "b": "Leonardo da Vinci",
        "c": "Raphael",
        "d": "Vincent van Gogh",
        "correct": "b"
    },
    {
        "q": "What is the capital of Japan?",
        "a": "Seoul",
        "b": "Kyoto",
        "c": "Tokyo",
        "d": "Osaka",
        "correct": "c"
    },
    {
        "q": "In computing, what does 'HTTP' stand for?",
        "a": "HyperText Transfer Protocol",
        "b": "High Transmission Text Program",
        "c": "HyperText Transmission Process",
        "d": "Host Transfer Type Protocol",
        "correct": "a"
    },
    {
        "q": "Which scientist proposed the three laws of motion?",
        "a": "Albert Einstein",
        "b": "Isaac Newton",
        "c": "Galileo Galilei",
        "d": "Nikola Tesla",
        "correct": "b"
    },
    {
        "q": "Which country has the longest coastline in the world?",
        "a": "Russia",
        "b": "Australia",
        "c": "Canada",
        "d": "Indonesia",
        "correct": "c"
    },
    {
        "q": "What is the smallest prime number greater than 100?",
        "a": "101",
        "b": "103",
        "c": "107",
        "d": "109",
        "correct": "a"
    },
    {
        "q": "Which physicist developed the uncertainty principle?",
        "a": "Werner Heisenberg",
        "b": "Erwin Schrödinger",
        "c": "Max Planck",
        "d": "Niels Bohr",
        "correct": "a"
    }
]

def main():
    results = {}
    while True:
        player_name = input("Enter your name: ")
        score = play_game()
        # check if score exists
        if results.get(player_name,None) is None:
            results[player_name] = score
        # if so check if last score is bigger 
        elif score > results[player_name]:
            # and overwite if so
            results[player_name] = score
        print("\n\nPLAYER HIGH SCORES...")
        for player in results.keys():
            print(f"{player} --- {results[player]}")

if __name__ == "__main__":
    main()
