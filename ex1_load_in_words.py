
def load_valid_words():
    valid_words = []

    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            valid_words.append(line)

    return valid_words 


if __name__ == "__main__":    
    words = load_valid_words()
    print(words[:15])