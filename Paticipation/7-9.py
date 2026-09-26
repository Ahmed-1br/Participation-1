#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the 
#list at least three times. Add code near the beginning of your program to print a message saying 
#the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' 
#from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

#step one, make list
sandwich_orders = ["Tuna", "Pastrami", "Chicken", "Pastrami", "Turkey", "Pastrami"]
#step two, print statement
print("The deli has run out of Pastrami.")
#step three, remove all occurrences of 'pastrami'
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
#step four, make finished sandwiches
finished_sandwiches =[]
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)