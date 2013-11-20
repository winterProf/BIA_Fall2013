
from palindrome_solution import ispalindrome


if __name__ == "__main__":
    print "Starting test of ispalindrome function"
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
