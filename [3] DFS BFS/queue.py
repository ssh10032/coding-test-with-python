# 파이썬에서 queue를 구현할 때에는
# collections 모듈의 dequeue를 사용
# >> 데이터를 넣고 빼는 속도가 list보다 효율적임
# list 메서드를 이용해서 list로 변경 가능
# ex) list(deque)

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()

print(queue)