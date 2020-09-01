import random

#A list of students
students_present = ["tommy", "dahlia", "manaia", "isaac", "jamila", "britt", "patrick", "jessika", "chantal", "rocio"]

#We need to pick 3 students from the list
print(students_present[0:3])

#A list of cards
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Print the first 5 cards
print(cards[0:5])

#Shuffle the cards
random.shuffle(cards)

#Print the first 5 cards again
print(cards[0:5])
