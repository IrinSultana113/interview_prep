class EvenSquares():
    def __init__(self):
        self.nums = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.nums <= 20:
          val = self.nums
          self.nums += 1
          if val % 2 == 0:
            return val ** 2
        
        raise StopIteration
        
for i in EvenSquares():
    print(i)

