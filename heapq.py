class MaxHeap(object):

    def __init__(self):
        self.heap = [10000000000]
        self.currentSize = 0

    def sift_UP(self, i):

        while i > 0:
            if self.heap[i] > self.heap[i // 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = tmp
            i = i // 2

    def sift_DOWN(self, i):

        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heap[i] < self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def Insert(self, k):
        self.heap.append(k)
        self.currentSize += 1
        self.sift_UP(self.currentSize)

    def ExtractMax(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        self.sift_DOWN(1)
        return retval


def main():
    bh = MaxHeap()
    k = int(input())
    for _ in range(k):
        str = input().split()
        if str[0] == 'Insert':
            bh.Insert(int(str[1]))
        if str[0] == 'ExtractMax':
            print(bh.ExtractMax())


if __name__ == "__main__":
    main()
