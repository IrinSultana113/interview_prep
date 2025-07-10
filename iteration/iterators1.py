class TopTen:  #TopTen is a iterable object. Because the TopTen class has __iter__ method.

    def __init__(self):
        self.nums = 1

    def __iter__(self):  # called the iter() method. and this method returns itself. as a result topten is a iterator
        return self
    
    def __next__(self): # then iterator calls the next method. then it returns the 1st element in the iterator. when  self.nums <= 10,  then  raise StopIteration. as a result for loop silently stop.

        if self.nums <= 10:
            val = self.nums
            self.nums += 1

            return val
        
        else:
            raise StopIteration
        
for i in TopTen(): # when next() method give one element. it is stored in i value. then print i
    print (i)
