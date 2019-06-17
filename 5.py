#program to perform different set operations like in mathematics

#define three sets
E={2,4,6,8}
N={1,2,3,4}
print("union of E and N is",E|N)
print("intersection of E and N",E&N)
print("Difference of N and E is",N-E)
print("Difference of E and N is",E-N)
print("symmetric difference E and N is",E^N)
print("symmetric difference N and E is",(E-N)|(N-E))
