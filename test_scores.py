#!/usr/bin/env python3

import statistics

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []

    while True:
        score = input("Enter test score: ")
        if score == "x":
            
            return scores
            
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")


def process_scores(scores):
    total = 0
    count = len(scores)
    #calculate total score
    for a in range(0, len(scores)):
        total = total + scores[a]

    # calculate average score

    average = total / count

    #minimum and maximum
    minimum = min(scores)
    maximum = max(scores)

    #calculate median score
    median = statistics.median(scores)

    # format and display the result
    print()
    print("Total:             ", total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low Score:         ", minimum, "\nHigh Score:        ", maximum)
    print("Madian Score:      ", median)
def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()