# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        # siftDown on parent node of the complete tree
        firstParentIdx = (len(array) - 1) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

            
    def siftDown(self, currentIdx, endIdx, heap):
        # Write your code here.
        leftChildIdx = 2*currentIdx + 1 
        while leftChildIdx <= endIdx:
            rightChildIdx = 2*currentIdx + 2 if currentIdx*2 + 2 <= endIdx else -1
            if rightChildIdx != -1 and heap[rightChildIdx] < heap[leftChildIdx]:
                idxSwap = rightChildIdx
            else:
                idxSwap = leftChildIdx
            if heap[currentIdx] > heap[idxSwap]:
                self.swap(currentIdx, idxSwap, heap)
                currentIdx = idxSwap
                leftChildIdx = 2*currentIdx + 1 
            

        while currentIdx <= endIdx and heap[currentIdx] > heap[leftChildIdx] and heap[currentIdx] > heap[rightChildIdx]:
            if heap[leftChildIdx] < heap[rightChildIdx]:
                self.swap(currentIdx, leftChildIdx, heap)
                currentIdx = leftChildIdx
                leftChildIdx = (2*currentIdx + 1) // 2
            else:
                self.swap(currentIdx, rightChildIdx, heap)
                currentIdx = rightChildIdx
                rightChildIdx = (2*currentIdx + 2) // 2


    def siftUp(self, currentIdx, heap):
        # Write your code here.
        parentIdx = (currentIdx - 1) // 2  
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2 

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        swap(0, len(heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove
 
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
