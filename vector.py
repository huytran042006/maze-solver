class Vector:
    def __init__(self, capacity=4):
        self._data =[None] * capacity #b=[None,None,None,None]
        self._size = 0
        self._capacity = capacity

    def size(self):
        return self._size    

    def is_empty(self):
        return True if self._size == 0 else False

v = Vector(4)
print(v._data)          # kỳ vọng: [None, None, None, None]
print(v.size())          # kỳ vọng: 0
print(v.is_empty())      # kỳ vọng: True
print(v._capacity)       # kỳ vọng: 4