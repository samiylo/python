# Homework Week 1, Friday:

# Assignment One

# from collections import Counter

# user_input = input("Please type a word. ")

# print(Counter(user_input))


#  Assignment Two

user_input = input("Write a quote. ")

def word_count(index):
    count = {}
    words = index.split()
    for word in words:
        if word in count:
            count[word] += 1
        else: 
            count[word] = 1
    return count

tally = word_count(user_input)

print(word_count(user_input))

# Assignment Three

#sorted_keys =  sorted(tally.values(), reverse=True)
#print(sorted_keys)

#final_keys = tally[:3]
import operator
deez = dict(sorted(tally.items(), key=operator.itemgetter(1), reverse=True)[:3])
print(deez)

