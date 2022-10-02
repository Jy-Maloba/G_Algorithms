#call stack
def greet(name):
    print ("hello," + name + "!")
    greet2(name)
    print ("getting ready to say bye...")
    bye()

#This function greets you and then calls two other functions. Here are those two functions:

def greet2(name):
    print ("how are you, " + name + "?")
def bye():
    print ("ok bye!")

greet(input("enter your name"))