"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid")
        score = float(input("Enter score: "))
    grade = get_grade(score)
    print(grade)


def get_grade(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()