def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    # doing reverse DFS until we have a match
    if descendantOne is topAncestor or descendantTwo is topAncestor:
        return topAncestor

    ancestralLineOne = {}
    reverseDFS(descendantOne, ancestralLineOne)
    ancestralLineTwo = {}
    reverseDFS(descendantTwo, ancestralLineTwo)    

    for ancestor in ancestralLineOne:
        if ancestor in ancestralLineTwo:
            return ancestor.name
    return None
        
def reverseDFS(ancestor, ancestralLine):
    ancestralLine[ancestor] = True
    nextAncestor = ancestor.ancestor
    if nextAncestor is not None:
        reverseDFS(nextAncestor, ancestralLine)
    return    

class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addAsAncestor(self, descendants):
        for descendant in descendants:
            descendant.ancestor = self

if __name__ == '__main__':
    
        
    ancestralTrees = {}
    ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for letter in ALPHABET:
        ancestralTrees[letter] = AncestralTree(letter)
    ancestralTrees["A"].addAsAncestor(
        [
            ancestralTrees["B"],
            ancestralTrees["C"],
            ancestralTrees["D"],
            ancestralTrees["E"],
            ancestralTrees["F"],
        ]
    )
    ancestralTrees["B"].addAsAncestor(
        [ancestralTrees["G"], ancestralTrees["H"], ancestralTrees["I"]]
    )
    ancestralTrees["C"].addAsAncestor([ancestralTrees["J"]])
    ancestralTrees["D"].addAsAncestor([ancestralTrees["K"], ancestralTrees["L"]])
    ancestralTrees["F"].addAsAncestor([ancestralTrees["M"], ancestralTrees["N"]])
    ancestralTrees["H"].addAsAncestor(
        [ancestralTrees["O"], ancestralTrees["P"], ancestralTrees["Q"], ancestralTrees["R"]]
    )
    ancestralTrees["K"].addAsAncestor([ancestralTrees["S"]])
    ancestralTrees["P"].addAsAncestor([ancestralTrees["T"], ancestralTrees["U"]])
    ancestralTrees["R"].addAsAncestor([ancestralTrees["V"]])
    ancestralTrees["V"].addAsAncestor(
        [ancestralTrees["W"], ancestralTrees["X"], ancestralTrees["Y"]]
    )
    ancestralTrees["X"].addAsAncestor([ancestralTrees["Z"]])


    print(getYoungestCommonAncestor(
                 ancestralTrees["A"], ancestralTrees["B"], ancestralTrees["F"]
                  ))
