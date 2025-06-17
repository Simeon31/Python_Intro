from collections import deque
queue = deque([])

queue.append(0)
queue.append(1)
queue.append(2)

queue.popleft()
# queue.popleft()
# queue.popleft()


print(*queue)

if not queue:
    print("Empty")