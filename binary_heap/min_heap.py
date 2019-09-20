class MinHeap:
    arr = [None]
    length = 0

    # Insert an item into the MinHeap while keeping the heap structure.
    def insert(self, item):
        if self.length + 1 >= len(self.arr):
            self.expand()
        self.arr[self.length] = item
        self.length += 1

        i = self.length - 1
        while self.parent_is_bigger(i):
            # Swap parent and child.
            parent_index = self.parent(i)
            self.arr[i], self.arr[parent_index] = self.arr[parent_index], self.arr[i]
            i = parent_index

    # Removes the root of the MinHeap.
    def remove_min(self):
        if self.length == 0:
            return
        self.arr[0] = self.arr[self.length - 1]
        self.arr[self.length - 1] = None
        self.length -= 1

        i = 0
        smaller_child = self.smaller_child(i)
        while smaller_child != -1:
            # Swap parent and child.
            self.arr[i], self.arr[smaller_child] = self.arr[smaller_child], self.arr[i]
            smaller_child = self.smaller_child(i)
            
    # Returns the index of a smaller child given the index of a parent.
    # If parent is smaller than both children, return -1
    def smaller_child(self, index):
        if 2 * index + 2 >= self.length:
            return -1
            
        # Pick a smaller child
        if self.arr[2 * index + 1] < self.arr[2 * index + 2]:
            if self.arr[index] > self.arr[2 * index + 1]:
                return 2 * index + 1
        else:
            if self.arr[index] > self.arr[2 * index + 2]:
                return 2 * index + 2

        return -1

    # Returns if parent is bigger given the index of a child.
    def parent_is_bigger(self, index):
        if index == 0:
            return False

        parent_index = self.parent(index)
        if self.arr[parent_index] > self.arr[index]:
            return True
        else:
            return False

    # Returns the index of the parent given the index of a child.
    def parent(self, index):
        return int((index - 1) / 2)

    # Increases the size of self.arr
    def expand(self):
        for i in range(2 * len(self.arr)):
            self.arr.append(None)

    # Prints self.arr without any None objects.
    def __str__(self):
        output = "[" + str(self.arr[0])
        for i in range(1, len(self.arr)):
            if self.arr[i] is None:
                output += "]"
                return output
            output += ", " + str(self.arr[i])

        return output

min_heap = MinHeap()

min_heap.insert(1)
min_heap.insert(8)
min_heap.insert(2)
min_heap.insert(6)
min_heap.insert(7)
min_heap.insert(0)
min_heap.insert(12)

print(min_heap)

min_heap.remove_min()
print(min_heap)

min_heap.remove_min()
print(min_heap)

min_heap.remove_min()
print(min_heap)

min_heap.remove_min()
print(min_heap)

min_heap.remove_min()
print(min_heap)

min_heap.remove_min()
print(min_heap)