def isPalindrome(string):
    	#first way... slice according to even/odd number of characters
	
   # Write your code here.
    parity = len(string) % 2
    if parity == 0:
        for i in range(len(string)+parity):
            if string[i] != string[len(string)-i-1]:
                return False
        return True
    elif parity != 0:
        for i in range((len(string)//2)+parity):
            if string[i] != string[len(string)-i-1]:
                return False
        return True
#testcases don't cover fact that for {parity} = even
# checking first and last character on string return True lol 
if __name__ == '__main__':
    print(isPalindrome("abcdefghihgfeddcba"))
    #abcdefghihgfeddcba
    