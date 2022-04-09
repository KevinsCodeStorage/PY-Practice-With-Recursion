# Write code for algorithm 5 below
def isPalindrome(word):

    if len(word) < 2:
        return True

    else:
        if word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        else:
            return False


sample_word = 'kayak'
print(isPalindrome(sample_word))
