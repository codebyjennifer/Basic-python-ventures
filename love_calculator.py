print("""
.__                       _________        .__               .__          __                 ._. ._.
|  |   _______  __ ____   \_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________  | | | |
|  |  /  _ \  \/ // __ \  /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \ | | | |
|  |_(  <_> )   /\  ___/  \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/  \|  \|
|____/\____/ \_/  \___  >  \______  (____  /____/\___  >____/|____(____  /__|  \____/|__|     __  __
                      \/          \/     \/          \/                \/                     \/  \/"""
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
