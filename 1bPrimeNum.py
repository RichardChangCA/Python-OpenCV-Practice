#打印100000以内所有的素数
import math
#for i in range(2, 100000 + 1):
#    for j in range(2, i+1):
#        if(j == i): # do not use j is i -> max is 256
#            print(i)
#        elif i % j == 0:
#            break
#        else:
#            pass



for i in range(2 ,100 + 1):
    for j in range(2, int(math.sqrt(i)) + 2):
        if(j == int(math.sqrt(i)) + 1): 
            print(i)
        elif i % j == 0:
            break
        else:
            pass
