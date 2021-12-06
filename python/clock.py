import time
 
def chunks(l, n=5):
    # returns a list of 'chunks' where each 'chunk' is of length n (default is 5)
    return [l[i:i+n] for i in range(0, len(l), n)]
 
def binary(n, digits=8):
    # actually only need 6 digits cuz max number to be represented from a digital clock is 60 (2^6 = 64 > 60)
    n=int(n)
    return '{0:0{1}b}'.format(n, digits)
 
def secs(n):
    n=int(n)
    h='x' * n
    return "|".join(chunks(h))
 
def bin_bit(h):
    h=h.replace("1","x")
    h=h.replace("0"," ")
    return "|".join(list(h))
 
 
x = str(time.ctime()).split()
print(x)
tyme = x[3].split(":")
scds =tyme[-1]
tyme=map(binary,tyme[:-1])
tyme = list(tyme)
print(bin_bit(tyme[0]))
print(" ")
print(bin_bit(tyme[1]))
print(" ")
print(secs(scds))