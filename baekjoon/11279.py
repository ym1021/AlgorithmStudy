import sys
import heapq

num = int(input())
heap = []
for _ in range(num):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, (-n))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)