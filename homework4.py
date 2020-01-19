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

print(word_count(user_input))
