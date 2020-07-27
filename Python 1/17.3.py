#Set up the sentence skeleton
SENTENCE = "I {} the {} {}"

#Ask user for words to put in sentence
verb = input("Please enter a verb (doing word): ")
adj = input("Please enter an adjective (describing word): ")
noun = input("Please enter a noun (thing): ")

#Print out sentence.
print(SENTENCE.format(verb, adj, noun))

