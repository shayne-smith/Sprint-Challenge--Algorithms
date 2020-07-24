'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # base case
    if len(word) < 2:
        return 0
    
    if f"{word[0]}{word[1]}" == "th":
        return 1 + count_th(word[2:])

    else:
        return count_th(word[1:])


if __name__ == '__main__':

    word = ""
    print("Count is: " + str(count_th(word)))

    word = "abcthxyz"
    print("Count is: " + str(count_th(word)))

    word = "abcthefthghith"
    print("Count is: " + str(count_th(word)))

