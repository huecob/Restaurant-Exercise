"""Restaurant rating lister."""

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

sorted_ratings_list = sorted(restaurant_and_ratings.items())
#sorting the dictionary .items() + sorted()

for name, ratings in sorted_ratings_list:
    print(f"{name} is rated at {ratings}")


