# Homework Assignment One - Tip Calculator

#Calculator 1

total_bill = float(input("Insert total bill ammount >>"))
# level_of_service = input("How was the service; good, fair or bad?")

# if level_of_service == "good":
#     total_bill *= 1.2
#     print("This will add 20% to the total bill.")
# elif level_of_service == "fair":
#     total_bill *= 1.5
#     print("This will add 15% to the total bill.")
# elif level_of_service == "bad":
#     total_bill *= 1.1
#     print("This will add 10% to the total bill.")
# else:
#     print("Do I look like I care?")

# Calculator 2

total_persons = int(input("How many people to split between?"))

split_pay = total_bill / total_persons


print("Each person will pay " + str(split_pay))
