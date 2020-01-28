# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    #tests on appropriate use of dictionary data structure in python
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSuffixAtIndex(i, string)
            
    def insertSuffixAtIndex(self, i, string):
        currentNode = self.root
        for j in range(i, len(string)):
            char = string[j]
            if char not in currentNode:
                currentNode[char] = {}
            currentNode = currentNode[char]
        currentNode[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node
        
if __name__ == '__main__':
    word1 = "test"
    test1 = SuffixTrie(word1)
    trie1 = {
        "e": {"s": {"t": {"*": True}}},
        "s": {"t": {"*": True}},
        "t": { "t":{"*":True}, "e": {"s": {"t": {"*": True}}}}
    }
    for i in reversed((range(len(word1)))): #order is reversed because we are testing for suffix substrings 
        substring = word1[i:]
        print(test1.contains(substring))



        
    
        
        
