import heapq

minheap = []
x = heapq.heapify(minheap)
print(x)


heapWithValues = [3, 1, 2]
# 将给定列表转换成最小堆
heapq.heapify(heapWithValues)
print(heapWithValues)

maxHeap = [1, 2, 3]
# 通过输入负值来获取最大堆
maxHeap = [-x for x in maxHeap]
heapq.heapify(maxHeap)
print(maxHeap)
heapq.heappush(maxHeap, -4)
print(maxHeap, type(maxHeap), maxHeap[0])


