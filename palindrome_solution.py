#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
import re

def ispalindrome(input):
    ispal = True
    i = 0
    j = len(input) - 1
    while (j >= i):
        while not re.match('\w+',input[i]) and i < j:
            i += 1
        while not re.match('\w+',input[i]) and j > i:
            j -= 1
        if input[i].lower() == input[j].lower():
            i += 1
            j -= 1
        else:
            ispal = False
            i = 1
            j = 0

    return ispal

if __name__ == "__main__":
    print "Starting test of ispalindrome function"
#    assert(ispalindrome("1234") == True)
    assert(ispalindrome("toot") == True)
    assert(ispalindrome("fart") == False)
    assert(ispalindrome("racecar") == True)
    assert(ispalindrome("race car") == True)
    assert(ispalindrome("Race Car") == True)
    assert(ispalindrome("Race a car") == False)
    print "Success on main parts"
    print "Testing first bonus"
    assert(ispalindrome("A man, a plan, a canal = Panama!") == True)
    print "Testing second bonus"
    print ispalindrome("")
