def IsRotation(string1, string2):
    if len(string1) != len(string2): #empty string case missed
        return False
    j = 0
    for i in range(len(string2)):
        if string2[i] == string1[0]:
            firstPart = string2[i:]
            secondPart = string2[:i]
            rotatedStr2 = firstPart + secondPart
            if rotatedStr2 == string1:
                return True
    return False

if __name__ == '__main__':
    print(IsRotation("abcdeee", "cdeeeab"))
    #problem context different
    

                