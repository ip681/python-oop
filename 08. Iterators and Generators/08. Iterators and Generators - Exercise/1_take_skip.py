class take_skip:
    def __init__(self,step,count):
        self.step = step
        self.count = count
        self.number=0
        self.counter=0
    def __iter__(self):
        return self

    def __next__(self):
        while self.counter<self.count:
            if self.counter >=1:
                self.number+=self.step
                self.counter+=1
                return self.number
            else:
                self.counter += 1
                return self.number

        raise StopIteration