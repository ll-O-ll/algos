import string as s
def caesarCipherEncryptor(string, key):
    # Write your code here.
    #if there's a notion of cycling -> use mod
    offset = len(string)
    alpha = list(s.ascii_lowercase)
    key = key % len(alpha)
    for i in range(len(string)):
        index = alpha.index(string[i])
        shift = (index + key) % len(alpha)
        string = string + alpha[shift]
    return string[offset:]


if __name__ == '__main__':
    print(caesarCipherEncryptor("xyz",2))
