from collections import Counter
from collections import List
from collections import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = []
        for count in counts.values():
            maxHeap.append(-count)

        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1

            if not maxHeap:
                time = queue[0][1]
            else:
                current = heapq.heappop(maxHeap) + 1
                if current:
                    queue.append((current, time + n))

            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0])
        

        return time