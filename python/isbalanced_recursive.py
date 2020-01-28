def is_balanced(s, counter = 0):
    if not s:
        return counter == 0
    #to save call stacks include following case:
    if counter < 0:
        return False
    if s[0] == "(":
        counter+=1
    elif s[0] == ")":
        counter -=1
    return is_balanced(s[1:],counter)
if __name__ == "__main__":

    string = "))()()"
    print(is_balanced(string))