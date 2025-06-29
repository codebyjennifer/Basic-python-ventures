print("True Love Calculator!")
user_name = input("What's your name?\n")
lover_name = input(f"Hi {user_name}! What's your lover's name?\n")

def calculate_love_score(name1,name2):
    chars = ""
    char = ""
    for letter in (name1 + name2).lower():
        if letter in "true":
            chars += letter
    love_degree = len(chars)
    for letter in (name1 + name2).lower():
        if letter in "love":
            char += letter
    love_degree2 = len(char)
    print(f"Your love score: {love_degree}{love_degree2}")
calculate_love_score(name1 = user_name, name2 = lover_name)
