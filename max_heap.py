class MaxHeap:

    heap =[]

    def create_minheap():
        pass

    def convert_to_maxheap(self, arr):
        self.convert_to_heap(arr)
    
    def convert_to_heap(self, arr):
        self.heap = arr
        lastIdx = int(len(self.heap)-1)
        i =  self.parent(lastIdx)
        while i >= 0:
            self.shift_down(i)
            i -= 1

    def shift_down(self,currentIdx):
        endIdx = len(self.heap)-1
        leftIdx = self.left_child(currentIdx)

        while leftIdx <= endIdx:
            rightIdx = self.right_child(currentIdx)
            idxToShift = int()

            if rightIdx <= endIdx and self.heap[rightIdx] > self.heap[leftIdx]:
                idxToShift = rightIdx
            else:
                idxToShift = leftIdx

            if self.heap[currentIdx] < self.heap[idxToShift]:
                #swaping the two element in the list
                self.heap[idxToShift], self.heap[currentIdx] = self.heap[currentIdx], self.heap[idxToShift]
                currentIdx = idxToShift
                leftIdx = self.left_child(currentIdx)
            else:
                return
        
        

    def shift_up(self, currentIdx):
        parentIdx = self.parent(currentIdx)

        while currentIdx > 0 and self.heap[parentIdx] < self.heap[currentIdx]:
            self.heap[currentIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[currentIdx]
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)

    def peek(self):
        if self.heap:
            return print(self.heap[0])
        else:
            return 'no value in the heap'

    def remove(self):
        if self.heap:
            lastIdx = len(self.heap)-1
            self.heap[0], self.heap[lastIdx] = self.heap[lastIdx], self.heap[0]
            del self.heap[lastIdx]
            self.shift_down(0)
            
        else:
            return 'no value in the heap'

    def insert(self, val):
        self.heap.append(val)
        lastIdx = len(self.heap)-1
        self.shift_up(lastIdx)

    def parent(self, i):
        idx = round((i - 1)/2)
        return idx

    def left_child(self, i):
        idx = (i*2) + 1
        return idx

    def right_child(self, i):
        idx = (i*2) + 2
        return idx

    def display(self):
        print(self.heap)
        



arr = [6,2,8,78,34]
heap1 = MaxHeap()
heap1.convert_to_maxheap(arr)
heap1.insert(5)
heap1.insert(54)
heap1.insert(9)
heap1.insert(67)
heap1.display()
heap1.remove()
print('heap after remove :')
heap1.display()

# heap1.peek()