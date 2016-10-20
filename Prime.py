def is_prime(x):
    count = 0
    if(x<3):
        if x==2:
            return True
        else:
            return False

    else:
        i = 2
        for i in range(2,x-1):
            if(x % i == 0):
                count=count+1
        if count>0:
            return False
        else:
            return True
print is_prime(5)
