def nth_prime(m):
        count=0
        num=2
        while True:
            if check_prime(num):
                count+=1
                if count==m:
                    return num
            num+=1