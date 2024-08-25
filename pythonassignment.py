# 1.Python programme to check whether a string is a palindrome or not
def is_palindrome(s):
 stack=[]
 #Add all the characters into the stack
 for char in s:
  stack.append(char)
  for char in s:
 #compare the stack with the original string
   stack.append(char)
   if char!=stack.pop():
    return False
   return True
#get the input string from the user
user_input=input("Enter a word to check if it is a palindrome: ")
#check if the input from the user is a palindrome
if is_palindrome(user_input):
 print(f"The word '{user_input}' is a palindrome")
else:
 print(f"The word '{user_input}' is not a palindrome")



#2.List comprehension
#It is a coincise way to create lists in python.
#examples is a as below for 
#a.Creating for filtering even numbers.
even=[x for x in range (10) if x % 2==0]
print(even)
#b.Creating a list for tuples
tuples =[(x,x**2) for x in range(5)]
print(tuples)
#c.Creating a list of squares
squares=[x**2 for x in range (10)]
print (squares)



#3Compound data types are data types that can hold more than two values.Here are three examples of compound data types
#a.Lists-this is simply an ordered collection of items.
list=[1,2,3,4]
#b.Tuples-an ordered collection of items.
tuple=(1,2,3,4)
#c.Dictionary-this is an unordered collection of key-value pairs.
dict={"name":"John","age":30,"city":"New York"}



#4.Function that takes a string and returns a list of bigrams-A bigram is a sequence of two adjascent elements from a string of text
def bigrams(s):
 bigrams = [s[i:i+2] for i in range(len(s)-1)]
 return bigrams
# Example usage:
input_str = "python"
print(bigrams(input_str))



#Function to Find the Closest Key in a Dictionary
def closest_key(d, value):
    closest = None
    for key, values in d.items():
        if value in values:
            if closest is None or values.index(value) < d[closest].index(value):
                closest = key
    return closest

# Example usage
my_dict = {'a': ['x', 'y', 'z'], 'b': ['u', 'v', 'w'], 'c': ['p', 'q', 'r']}
print(closest_key(my_dict, 'v'))

