class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None

    # Add your code here
    def computeDifference(self):
        size = len(self.__elements)
        maxx = -99
        for i in range(size):
            for j in range(size):
                val = abs(self.__elements[i] - self.__elements[j])
                if val > maxx:
                    maxx = val
        self.maximumDifference = maxx
        #return maximumDifference
                        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)