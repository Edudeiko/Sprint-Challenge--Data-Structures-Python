class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.max = [None for i in range(capacity)]

    def append(self, item):
        self.max[self.current] = item
        self.current += 1
        if self.current > self.capacity -1:
            self.current = 0

    def get(self):
        return [ii for ii in self.max if ii is not None]
