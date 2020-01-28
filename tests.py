import time

def check_prime(num):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            res = True
    return res


def check_prime_verbose(num):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", time.time()-t1)
                break
        else:
            print(num,"is a prime number")
            print("Time:", time.time()-t1) 
            res = True
    return res