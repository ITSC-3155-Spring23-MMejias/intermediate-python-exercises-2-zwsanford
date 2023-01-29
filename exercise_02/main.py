import math, time

startTime = time.time()

def fib(num):
    if(num >= 15 and num <= 35):
        val = (1/math.sqrt(5)) * pow((1+math.sqrt(5))/2,num) - (1/math.sqrt(5)) * pow((1-math.sqrt(5))/2,num)
        return int(val)
    else:
        return 0

print("fib(34) =" + str(fib(34)))
print("fib(34) =" + str(time.time()-startTime) + " seconds")