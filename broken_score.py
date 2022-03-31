import random


def main():
    filename = "results.txt"
    out_file = open(filename, "w")

    while True:
        score = float(input("Enter score: "))
        """input -1 will be get 4 random number, input -2 will be finish loop"""
        if score == -1:
            num = 4
            for i in range(num):
                score = random.randint(0, 100)
                out_file.write(f"{score} is {determine_status(score)}\n")
            break
        elif score == -2:
            break
        else:
            out_file.write(f"{score} is {determine_status(score)}")

    out_file.close()


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
