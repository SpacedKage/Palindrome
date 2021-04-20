#Program to see if a word is a Palindrome. 
"""Input a word to see if its a Palindrome. The output will be either Yes or No"""

str = input("Please enter a word : ")

if(str == str[:: - 1]):
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")