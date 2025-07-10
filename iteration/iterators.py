nums = [1,2,3,4]  # nums is a list.  list, tuple, strings are  iterable objects

x = iter(nums) # this iter() converted the nums object to a iterator. iter(nums) internally calls nums.__iter__() and returns an iterator object. so now x is a iterator 

print(next(x)) # x iterator calls the next() method. then it returns the 1st element in the iterator.
               # output: 1
print(next(x)) # then again x iterator calls the next() method. then it returns the next element in the iterator. 
               #output: 2
               
#like this you can print one by one
print(next(x)) #outSput: 3

print(next(x)) #output: 4


