class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        out = []
        sorted_tasks = sorted([[x[0], x[1], i] for i, x in enumerate(tasks)])
        # insert all of the elements into the min heap
            # [processing_time, index, enqueue_time]
        heap = []
        curr_time = 0
        task_ptr = 0
        n = len(tasks)

        # init the start time
        # while the heap is not empty
        while task_ptr < n or heap:
            if not heap and curr_time < sorted_tasks[task_ptr][0]:
                curr_time = sorted_tasks[task_ptr][0]

            
            while task_ptr < n and curr_time >= sorted_tasks[task_ptr][0]:
                enq_time, proc_time, i = sorted_tasks[task_ptr]
                task_ptr += 1
                heapq.heappush(heap, (proc_time, i))
            
            proc_time, i = heapq.heappop(heap)
            curr_time += proc_time
            out.append(i)

        return out