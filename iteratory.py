import random
import operator
import time
from timeit import default_timer as timer

L1=[]
L2=[]

for i in range(10):
    L1.append(random.randint(1000000, 10000000000))

for i in range(10):
    L2.append(random.randint(1000000, 10000000000))

#t1=time.time_ns()
start = timer()
a, b, c, d, e, f, g, h, i, j = map(operator.mul, L1, L2)

#t2=time.time_ns()
end = timer()
print("Wyniki:", a, b, c, d, e, f, g, h, i, j)
#time_val_1=(t2-t1)
print("Czas na funkje map: ", str(end - start))


#t1=time.time_ns()
start = timer()
print("Wyniki : , " , end=" ")
for i in range(10):
    print(L1[i]*L2[i], end=" ")

end = timer()
#t2=time.time_ns()
#time_val_2=(t2-t1)
print("\nCzas na mnozenie funkcji: ", str(end - start))