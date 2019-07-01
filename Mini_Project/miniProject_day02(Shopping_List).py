# Shopping List App 

"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""


#   Make a list to hold onto our items.
shopping_list = []

# Print out instructions on how to use the app
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    
    # add new items to our list
    shopping_list.append(new_item)

#  print out the list
print("Here’s your list")
for item in shopping_list:
    print ( item )



"""
Challenge 2
    If I type SHOW, 
    I should be able to see what is currently in the list

    If I type HELP, 
    I should be able to see all the help for these special commands

Hint 2
    Step 1: Have a HELP command
    Step 2: Have a SHOW command
    Step 3: Add a function for adding into the list 
    Step 4: Cleanup the code in general
"""
shopping_list = []
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        print(shopping_list)
        continue
    elif new_item == 'HELP':
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'SHOW' see what is currently in the list.")
        continue
    else:
        shopping_list.append(new_item)
print("Here’s your list")
for item in shopping_list:
    print ( item )


"""

Challenge 3
    User can enter SHOW or Show or show, 
    similar for DONE and HELP, but the program should do the required job

    Show the item in the list serially starting from 1

    Let us accept items using a comma separated string
        
    Also there should be a functionality to add an item at a specific index

    There should be a functionality to remove items from the list at a specific index using REMOVE
    
    Do all the exception handling for all the extreme use cases 
"""
shopping_list = []
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")


item = list(map(str,input("Enter :").split(",")))
for new_item in item:
    if new_item.upper() == 'DONE':
        break
    elif new_item.upper() == 'SHOW':
        print(shopping_list)
            
    elif new_item.upper() == 'HELP':
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'SHOW' see what is currently in the list.")
            
    else:
        shopping_list.append(new_item)

print("Here’s your list")
for i in range(len(shopping_list)):
    print ( i+1,shopping_list[i] )
insert=input("Do you want to insert from list:")
if insert=="yes":
    index=int(input("enter specific index to insert :"))
    value=input("eneter value to insert")
    shopping_list.insert(index,value)
for i in range(len(shopping_list)):
    print ( i+1,shopping_list[i] )
    
remove=input("Do you want to remove from list:")
if remove=="yes":
    value1=input("enter specific value to delete :")
    shopping_list.remove(value1)
for i in range(len(shopping_list)):
    print ( i+1,shopping_list[i] )


"""
Challenge 4   
    Do all the exception handling for all the extreme use cases 
"""

"""
Challenge 5   
    Store the shopping list in a file. 
    
"""
with open('mini_day02.txt', 'w') as f:
    for item in shopping_list:
        f.write("%s\n" % item)
