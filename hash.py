#HASH TABLE
#A hash function is where you put in a string and you get back a number
#dictionary is an example of a hash table

#first approach
# book = dict()
# book["apple"] = 0.67
# book["milk"] = 1.49
# book["avocado"] = 1.49

#second approach in one line
book = {"apple": 0.67, "milk": 1.49, "avocado":1.49 }
print(book) #prints the entire hash table
print(book["apple"]) #returns the value of apple (0.67)

#phonebook
phone_book = dict()
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

new = phone_book.get("jenny")
print(new) #returns the value of jenny (8675309)

#checking if a person has already voted
voted = {} #hash table of people who have voted
def check_voter(name):
    if voted.get(name): #if they have already voted. (their name is in the voted table)
        print("kick them out!")
    else: #if their name is not in the voted hash table
        voted[name] = True #add their name.
        print("let them vote!")

#CACHING
#how websites use cache to save time
cache = {}
def get_data_from_server():
    pass

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

#the server only does the work of going to fetch the url if it is not cached
