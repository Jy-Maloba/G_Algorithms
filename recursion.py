#looking for a key in a pile of boxes inside one large box that have boxes in them
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not 0: #while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print ("found the key!")
# The second way uses recursion. Recursion is where a function calls itself.
# Here’s the second way in pseudocode:
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item) #Recursion!
        elif item.is_a_key():
            print ("found the key!")



#countdown function
def countdown(i):
    print (i)
    if i <= 0: #base case
        return
    else: #recursive case
        countdown(i-1)
    
countdown(10)

# recursion using call stack
#recursive function to calculate the factorial of a number
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1) # here's the recursive call