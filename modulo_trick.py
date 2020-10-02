def modulo(number, mod):
    while number >= mod:
        number -= mod
    return number

if __name__ == "__main__":
    number  = 23
    mod = 4
    print(modulo(number, mod))