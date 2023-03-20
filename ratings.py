"""Restaurant rating lister."""

import random

#create an empty dictionary variable
restaurant_and_ratings = {}
#open file = variable*
scores_data = open("scores.txt")
#split the lines by the delimiter :
for line in scores_data:
    white_space_gone = line.strip()
    individual_data = white_space_gone.split(":")
#loop through each line and
#add place [0] is rated at [1] to the dictionary
    restaurant_and_ratings[individual_data[0]] = individual_data[1]

while True:

    new_user_input = input("What would you like to do? Press [Q] to quit. [A] to add restaurant data. [S] to show all data. [R] to update random restaurant rating")
    if new_user_input == "Q" or new_user_input == "q":
        break

    elif new_user_input == "A" or new_user_input == "a":
        new_addition_restaurant = input("What is the restaurant name? ")
        new_score = input("What is the restaurant's score? ")

        try:
            new_score = int(new_score)

        except:
            new_scores = input("Please enter a valid score between 1 and 5: ")

        if new_score not in range(1,6):
            new_score = input("Please enter a valid score between 1 and 5 Or type Q to exit: ")

        restaurant_and_ratings[new_addition_restaurant] = new_score

    elif new_user_input == "S" or new_user_input == "s":

        sorted_ratings_list = sorted(restaurant_and_ratings.items())
#sorting the dictionary .items() + sorted()

        for name, ratings in sorted_ratings_list:
            print(f"{name} is rated at {ratings}")

    elif new_user_input == "R" or new_user_input == "r":
        restaurant_list = list(restaurant_and_ratings.keys())
        random_restaurant = random.choice(restaurant_list)
        new_user_rating = input(f"What would you like to update {random_restaurant}'s rating to?")
        restaurant_and_ratings[random_restaurant] = new_user_rating
        


