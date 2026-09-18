class Queue:
    def __init__(self, capacity=4):
        self._data = [None] * capacity
        self._size = 0
        self._capacity = capacity
        self._front = 0
        self._rear = 0

    def size(self):
        return self._size    

    def is_empty(self):
        return True if self._size == 0 else False

    def enqueue(self, value):
        if self._size == self._capacity:
            raise IndexError('Queue is full')
        self._data[self._rear] = value
        self._rear = (self._rear+1) % self._capacity
        self._size +=1

    def dequeue(self):
        if self._size == 0:
            raise IndexError('Queue is empty')
        output = self._data[self._front]
        self._front = (self._front+1) % self._capacity
        self._size -=1
        return output


q = Queue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
# q._data = [1,2,3,4], front=0, rear=0, size=4 (đầy)

x = q.dequeue()
print(x)                                  # kỳ vọng: 1
print(q._data, q._front, q._rear, q._size)
# kỳ vọng: [1, 2, 3, 4] 1 0 3   <- data KHÔNG bị xóa giá trị cũ, chỉ front di chuyển

q.enqueue(5)   # giờ enqueue lại được vì vừa dequeue, còn chỗ trống
print(q._data, q._front, q._rear, q._size)
# kỳ vọng: [5, 2, 3, 4] 1 1 4   <- 5 ghi đè đúng vào ô 0 (rear cũ)

try:
    q2 = Queue(2)
    q2.dequeue()
except Exception as e:
    print("Đúng, bị chặn:", e)
# kỳ vọng: in ra dòng lỗi vì Queue vừa tạo còn rỗng