class ArrayQueue:
  """ FIFO queue implementation using a Python list as underlying storage. """
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self.data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned


def radix_sort(l):
    """ do sorting the list l using radix algorithm and return back the list after sorted

    init division and mod"""
    division = 1
    mod = 10

    start = True
    while start:
        start = False
        """ Create array bucket with 10 queue. Each queue will contain all number have digit 
        (each loop while will from least significant digit to the most significant digit) respective 0 - 9.
        each digit in number will be in range [0-9], so we need 10 queues """
        bucket = []
        for i in range(0, 10):
            bucket.append(ArrayQueue())     # init queue for each bucket element

        """ Now, go though all number in list l, and put it respective to queue """
        for num in l:
            position = num % mod // division        # find the position of queue in bucket array for this number
            bucket[position].enqueue(num)           # put this number into position
            if not start and position > 0:          # check if no more digit to stop while loop
                start = True

        l = []                                      # init list l to put numbers back in order
        """ Now, push back element to list l by sorting the digit"""
        for bucknum in bucket:
            while not bucknum.is_empty():
                l.append(bucknum.dequeue())

        """ Increase the mod and division to do for next digit"""
        mod = mod * 10
        division = division * 10

    return l                                        # final, return the list l after sorted


if __name__ == '__main__':
    l = [35, 53, 55, 33, 52, 32, 25]
    print("Before sort is: ", l)        # output: [35, 53, 55, 33, 52, 32, 25]
    l = radix_sort(l)
    print("After sort is: ", l)         # output: [25, 32, 33, 35, 52, 53, 55]
