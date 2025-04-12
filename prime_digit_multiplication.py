def main(a):
    def check_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    def nth_prime(m):
        count=0
        num=2
        while True:
            if check_prime(num):
                count+=1
                if count==m:
                    return num
            num+=1
    q=nth_prime(a)
    q_count=0
    for i in q1:
        print("i=",i)
        q_count+=int(i)
    return q_count*a
print(main(5))
    