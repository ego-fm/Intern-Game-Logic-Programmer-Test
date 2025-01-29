class CircularBufferList:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.is_full = False

    def enqueue(self, item):
        if self.is_full:
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.is_full = self.head == self.tail

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None  # Очистка ссылки
        self.head = (self.head + 1) % self.size
        self.is_full = False
        return item

    def is_empty(self):
        return not self.is_full and self.head == self.tail

    def __repr__(self):
        return f"CircularBufferList({self.buffer})"
