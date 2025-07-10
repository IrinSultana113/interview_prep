class Countdown:
    def __init__(self):
        self.count = 5

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < 0:
            val = self.count
            self.count -= 5
            return val
        else: 
            raise StopIteration
        
for i in Countdown():
    print(i)

        