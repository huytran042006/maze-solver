class Vector:
    def __init__(self, capacity=4):
        self._data =[None] * capacity #b=[None,None,None,None]
        self._size = 0
        self._capacity = capacity

    def size(self):
        return self._size    

    def is_empty(self):
        return True if self._size == 0 else False

    def push(self, value):
        if self._size < self._capacity:
            pass
        else:
            new_capacity = self._capacity *2
            new_data = [None] * new_capacity
            for i in range(self._capacity):
                new_data[i] = self._data[i]
            self._capacity = new_capacity
            self._data = new_data
        self._data[self._size] = value
        self._size +=1

    def get(self, index):
        if index >= self.size():
            raise IndexError('Out of range')
        else:
            return self._data[index]


#print(v._data)           # [None, None, None, None]
#print(v.size())          # 0
#print(v.is_empty())      # True
#print(v._capacity)       # 4