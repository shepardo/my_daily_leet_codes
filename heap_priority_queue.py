
class HeapPriorityQueue:

    def __init__(self):
        self.a = []
        self.a.append(0)
        self.N = 0

    def insert(self, v):
        self.a.append(v)
        self.N += 1
        self.ascend_heap(self.N)
        #print(self.a)

    def ascend_heap(self, k):
        v = self.a[k]
        while self.a[int(k/2)] > v and k > 1:
            self.a[k] = self.a[int(k/2)]
            k = int(k / 2)
        self.a[k] = v

    def remove(self):
        v = self.a[1]
        self.a[1] = self.a[self.N]
        self.N -= 1
        self.descent_heap(1)
        self.a.pop()
        #print(self.a)
        return v

    def descent_heap(self, k):
        v = self.a[k]
        while k <= int(self.N / 2):
            j = k + k
            if (j < self.N) and (self.a[j] > self.a[j + 1]):
                j += 1
            if (v <= self.a[j]):
                break
            self.a[k] = self.a[j]
            k = j
        self.a[k] = v

def main():
    h = HeapPriorityQueue()
    h.insert(8)
    h.insert(6)
    h.insert(2)
    h.insert(3)
    print(h.remove())
    print(h.remove())
    print(h.remove())
    print(h.remove())

if __name__ == "__main__":
    main()
