def is_balanced(s):
    ''' Return True iff the parentheses in the string s are balanced'''

    count = 0

    #parse through list
    for i in range(len(s)):
        if count < 0: #if at any point we get no cancellation this means there is a ) in the prefix... false
            return False                                    #cannot start a string with )... dnm
        if s[i] == "(":
            count += 1
        elif s[i] == ")":
            count -= 1

    return count == 0
 
if __name__ == "__main__":

    string = "((((()))))"
    print(is_balanced(string))
