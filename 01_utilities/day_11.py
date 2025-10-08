"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""


def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10

    return min(score, 100)

def run_friendship_calculator():
    print("❤ Fiendship Compatibility calculator ❤")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)

    if score > 80:
        print("You're like chai and samosa — made for each other! 💖")
    elif score > 50:
        print("You're kind of a warm spices. 💥")
    else:
        print("Hey, maybe you're TEA and your friend is COFFEE. 🤣")


run_friendship_calculator()