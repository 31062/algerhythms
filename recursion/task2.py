def palindrome(word):
    #base sulution
    n = len(word)
    if n == 1:
        result = True
    #genral solution
    else:
        start = word[0]
        end = word[-1]
        if start == end:
            word = word[1:-2]
            palindrome(word)
        else:
            result = False
    return result

def user_input():
    word = input("plaese ebter a word")
    return word

def display(result):
    if result:
        print("the word is a palindrome")
    else:
        print("the word is not a palindrome")

def main
    
        
