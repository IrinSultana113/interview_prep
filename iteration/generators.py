def generator(): # write a function
    for i in range(1, 4): # i will take values 1,2,3
        yield i # yield recieves value 1 then pause. Send 1 whoever is using this generator. 
                # take one step, give one value, wait until asked again.

gen = generator()
for i in gen: 
        print(i)


        #Start the function
        #Run until yield i → return i (e.g., 1)
        # Pause
        # Next loop → resume from last yield
        # Repeat until there are no more values → then StopIteration is raised internally and the loop ends
