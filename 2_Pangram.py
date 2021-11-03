# Python3 program to
# Check if the string is pangram
import string
  
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
# Driver code
string = input("Enter your sentence:  ")
print("Let's see if your sentence is a pangram")
#string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes, it is")
else:
    print("No it's not")
