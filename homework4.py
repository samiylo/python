# Homework Week 1, Friday:

#Assignment One

empty_dict = {}
for letter in word:
    if letters not in word:
        empty_dict[letters] = 0
    empty_dict[letters] += 1
print(empty_dict)


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

print(tally)
