
# Homework Wednesday


# Excercise 1

# num = [1, 2, 3, 4, 5]
# num2 = [2, 3, 4, 5, 6]
# num3 = []
# for i in range (0, len(num)):
#     num3.append(num[i] * num2[i])
# print((num3))

# print(c)


# Excercise 2

# a = [[1,3],[2,4]]
# b = [[5,2], [1,0]]
# c = []

# for index1 in range(len(a)):
#     small_list = []
#     for number in range(len(a[index1])):
#         new_number = a[index1][number] + b[index1][number]
#         small_list.append(new_number)
#     c.append(small_list)
# print(c)

# Excercise 3 
#
#    Im assuming that I already formatted the funtion like that, so its gonna be the same.
#   

# a = [[1,3,4],[2,4,4]]
# b = [[5,2,2], [1,0,3]]
# c = []

# for index1 in range(len(a)):
#     small_list = []
#     for number in range(len(a[index1])):
#         new_number = a[index1][number] + b[index1][number]
#         small_list.append(new_number)
#     c.append(small_list)
# print(c)


# Excercise 4

# newlist=[]
# for item in original:
#     if item in newlist:
#         print ("You don't need to add "+str(item)+" again.")
#     else:
#         newlist.append(item)
#         print( "Added "+str(item))
# print (newlist)

# Excercise 5

# normal_sentence = "I am a leet programmer".upper()
# leet_list = list(normal_sentence)
# for i in range(len(leet_list)):
#     if leet_list[i] == 'A':
#         leet_list[i] = '4'
#     elif leet_list[i] == 'E':
#         leet_list[i] = '3'
#     elif leet_list[i] == 'G':
#         leet_list[i] = '6'
#     elif leet_list[i] == 'I':
#         leet_list[i] = '1'
#     elif leet_list[i] == 'O':
#         leet_list[i] = '0'
#     elif leet_list[i] == 'S':
#         leet_list[i] = '5'
#     elif leet_list[i] == 'T':
#         leet_list[i] = '7'
# leet_sentence = "".join(leet_list)
# print(leet_sentence.lower())


# shakespeare = """All that glitters is not gold
# Fair is foul, and foul is fair: Hover through the fog and filthy air.
# Life ... is a tale Told by an idiot, full of sound and fury, Signifying nothing."""
# shake_upper = shakespeare.upper()
# shake_list = list(shake_upper)
# leet_shake = []
# leet = {"A" : "4", "E" : "3", "G" : "6", "I" : "1", "O" : "0", "S" : "5", "T" : "7"}
# for letter in shake_upper:
#     if letter in leet:
#         letter = leet[letter]
#         leet_shake.append(letter)
#     else:
#         leet_shake.append(letter)
# final = "".join(leet_shake).lower()
# print(final)



# Excercise 6

# string_to_vowel_check = 'Good'
# last_letter = ''
# new_string = ''
# for letter in string_to_vowel_check:
#     is_vowel = False
#     if letter == last_letter:
#         if letter == 'a' or letter == 'A':
#             is_vowel = True
#         elif letter == 'e' or letter == 'E':
#             is_vowel = True
#         elif letter == 'i' or letter == 'I':
#             is_vowel = True
#         elif letter == 'o' or letter == 'O':
#             is_vowel = True
#         elif letter == 'u' or letter == 'U':
#             is_vowel = True
#     last_letter = letter
#     if is_vowel == True:
#         letter = letter*4
#     new_string+= letter
# print(new_string)

# Excercise 7

#I just cant seem to find the solution. I will try to get assistance tommorow.

